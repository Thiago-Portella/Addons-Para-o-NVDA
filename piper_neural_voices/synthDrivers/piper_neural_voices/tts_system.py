# coding: utf-8

# Copyright (c) 2023 Musharraf Omer
# This file is covered by the GNU General Public License.

import copy
import io
import json
import operator
import os
import re
import string
import sys
import tarfile
import typing
import wave
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Mapping, Optional, Sequence, Union

import globalVars


HERE = os.path.abspath(os.path.dirname(__file__))
LIB_DIRECTORY = os.path.join(HERE, "lib")
NVDA_ESPEAK_DIR = os.path.join(globalVars.appDir, "synthDrivers")
os.environ["PIPER_ESPEAKNG_DATA_DIRECTORY"] = os.fspath(NVDA_ESPEAK_DIR)
os.environ["ORT_DYLIB_PATH"] = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "lib", "onnxruntime.dll")
)


sys.path.insert(0, LIB_DIRECTORY)
from pathlib import Path
from pyper import Piper as PiperModel, SynthConfig, AudioOutputConfig
sys.path.remove(LIB_DIRECTORY)


PIPER_VOICE_SAMPLES_URL = "https://rhasspy.github.io/piper-samples/"
PIPER_VOICES_DIR = os.path.join(globalVars.appArgs.configPath, "piper", "voices")

FALLBACK_SPEAKER_NAME = "default"
DEFAULT_RATE = 50
DEFAULT_VOLUME = 100
DEFAULT_PITCH = 50


class VoiceNotFoundError(LookupError):
    pass


class SpeakerNotFoundError(LookupError):
    pass


class AudioTask(ABC):
    @abstractmethod
    def generate_audio(self) -> bytes:
        """Generate audio."""


class SilenceTask(AudioTask):
    __slots__ = ["time_ms", "sample_rate"]

    def __init__(self, time_ms, sample_rate):
        self.time_ms = time_ms
        self.sample_rate = sample_rate

    def generate_audio(self):
        """Generate silence (16-bit mono at sample rate)."""
        num_samples = int((self.time_ms / 1000.0) * self.sample_rate)
        return bytes(num_samples * 2)


@dataclass
class PiperVoice:
    key: str
    name: str
    language: str
    description: str
    location: str
    properties: typing.Optional[typing.Mapping[str, int]] = field(default_factory=dict)

    def __post_init__(self):
        try:
            self.model_path = next(self.location.glob("*.onnx"))
            self.config_path = next(self.location.glob("*.onnx.json"))
        except StopIteration:
            raise RuntimeError(
                f"Could not load voice from `{os.fspath(self.location)}`"
            )
        self.model = PiperModel(
            os.fspath(self.config_path), os.fspath(self.model_path)
        )
        self.config = PiperConfig.load_from_json_file(self.config_path)
        self.speakers = self.config.speaker_id_map

    @property
    def is_multi_speaker(self):
        return bool(self.speakers)

    @property
    def default_speaker(self):
        try:
            rev_speaker_map = { v: k for (k, v) in self.speakers.items() }
            return rev_speaker_map[0]
        except KeyError:
            try:
                return next(iter(self.speakers))
            except StopIteration:
                raise SpeakerNotFoundError(f"Voice `{self.name}` has no speakers")

    def synthesize(self, text, speaker, rate, volume, pitch):
        synth_config = SynthConfig(speaker=speaker)
        audio_output_config = AudioOutputConfig(
            rate=rate,
            volume=volume,
            pitch=pitch
        )
        return self.model.synthesize_batched(text, synth_config=synth_config, audio_output_config=audio_output_config, batch_size=6)


class SpeechOptions:
    __slots__ = ["voice", "speaker", "rate", "volume", "pitch"]

    def __init__(self, voice, speaker=None, rate=None, volume=None, pitch=None):
        self.voice = voice
        self.speaker = speaker
        self.rate = rate
        self.volume = volume
        self.pitch = pitch

    def set_voice(self, voice: PiperVoice):
        self.voice = voice
        if voice.is_multi_speaker:
            self.speaker = voice.default_speaker
        else:
            self.speaker = None

    def copy(self):
        return copy.copy(self)

    def speak_text(self, text):
        return self.voice.synthesize(
            text,
            self.speaker,
            self.rate,
            self.volume,
            self.pitch,
        )


@dataclass
class PiperSpeechSynthesisTask(AudioTask):
    """A pending request to synthesize a token."""

    __slots__ = ["text", "speech_options"]

    def __init__(self, text, speech_options):
        self.text = text
        self.speech_options = speech_options

    def generate_audio(self):
        return self.speech_options.speak_text(self.text)


class PiperTextToSpeechSystem:

    VOICE_NAME_REGEX = re.compile(
        r"voice(-|_)(?P<language>[a-z]+[-]?([a-z]+)?)(-|_)(?P<name>[a-z]+)(-|_)(?P<quality>(high|medium|low|x-low))"
    )

    def __init__(
        self, voices: Sequence[PiperVoice], speech_options: SpeechOptions = None
    ):
        self.voices = voices
        if speech_options is None:
            try:
                voice = self.voices[0]
            except IndexError:
                raise VoiceNotFoundError("No Piper voices found")
            self.speech_options = SpeechOptions(voice=voice)
        else:
            speech_options = speech_options

    def shutdown(self):
        pass

    @property
    def voice(self) -> str:
        """Get the current voice key"""
        return self.speech_options.voice.key

    @voice.setter
    def voice(self, new_voice: str):
        """Set the current voice key"""
        for voice in self.voices:
            if voice.key == new_voice:
                self.speech_options.set_voice(voice)
                return
        raise VoiceNotFoundError(
            f"A voice with the given key `{new_voice}` was not found"
        )

    @property
    def speaker(self) -> str:
        """Get the current speaker"""
        return self.speech_options.speaker or FALLBACK_SPEAKER_NAME

    @speaker.setter
    def speaker(self, new_speaker: str):
        if new_speaker == FALLBACK_SPEAKER_NAME:
            return
        if new_speaker in self.speech_options.voice.speakers:
            self.speech_options.speaker = new_speaker
        else:
            raise SpeakerNotFoundError(f"Speaker `{new_speaker}` was not found")

    @property
    def language(self) -> str:
        """Get the current voice language"""
        return self.speech_options.voice.language

    @language.setter
    def language(self, new_language: str):
        """Set the current voice language"""
        lang = self.normalize_language(new_language)
        lang_code = lang.split("-")[0] + "-"
        possible_voices = []
        for voice in self.voices:
            if voice.language == lang:
                self.speech_options.set_voice(voice)
                return
            elif voice.language.startswith(lang_code):
                possible_voices.append(voice)
        if possible_voices:
            self.speech_options.set_voice(possible_voices[0])
            return
        raise VoiceNotFoundError(
            f"A voice with the given language `{new_language}` was not found"
        )

    @property
    def volume(self) -> float:
        """Get the current volume in [0, 100]"""
        return self.speech_options.volume or DEFAULT_VOLUME

    @volume.setter
    def volume(self, new_volume: float):
        """Set the current volume in [0, 100]"""
        self.speech_options.volume = new_volume

    @property
    def rate(self) -> float:
        """Get the current speaking rate in [0, 100]"""
        return self.speech_options.rate or DEFAULT_RATE

    @rate.setter
    def rate(self, new_rate: float):
        """Set the current speaking rate in [0, 100]"""
        self.speech_options.rate = new_rate

    @property
    def pitch(self) -> float:
        """Get the current speaking pitch in [0, 100]"""
        return self.speech_options.pitch or DEFAULT_PITCH

    @pitch.setter
    def pitch(self, new_pitch: float):
        """Set the current speaking pitch in [0, 100]"""
        self.speech_options.pitch = new_pitch

    def get_voices(self):
        return self.voices

    def get_speakers(self):
        speakers = list(self.speech_options.voice.speakers)
        return [FALLBACK_SPEAKER_NAME, *speakers]

    def create_speech_task(self, text):
        return PiperSpeechSynthesisTask(text, self.speech_options.copy())

    def create_break_task(self, time_ms):
        return SilenceTask(time_ms, self.speech_options.voice.config.sample_rate)

    @staticmethod
    def normalize_language(language):
        language = language.replace("_", "-")
        lang, *localename = language.split("-")
        if not localename:
            return lang
        else:
            localename = localename[0].upper()
            return "-".join([lang, localename])

    @classmethod
    def load_piper_voices_from_nvda_config_dir(cls):
        Path(PIPER_VOICES_DIR).mkdir(parents=True, exist_ok=True)
        return sorted(
            cls.load_voices_from_directory(PIPER_VOICES_DIR),
            key=operator.attrgetter("name"),
        )

    @classmethod
    def load_voices_from_directory(cls, voices_directory, *, directory_name_prefix="voice-"):
        rv = []
        for directory in (d for d in Path(voices_directory).iterdir() if d.is_dir()):
            match = cls.VOICE_NAME_REGEX.match(directory.name)
            if match is None:
                continue
            info = match.groupdict()
            language = cls.normalize_language(info["language"])
            name = info["name"]
            quality = info["quality"]
            rv.append(
                PiperVoice(
                    key=f"{language}-{name}-{quality}",
                    name=name.title(),
                    language=language,
                    description="",
                    location=directory.absolute(),
                    properties={"quality": quality},
                )
            )
        return rv

    @classmethod
    def install_voice(cls, voice_archive_path, dest_dir):
        """Uniform handleing of voice tar archives."""
        archive_path = Path(voice_archive_path)
        voice_name = archive_path.name.rstrip("".join(archive_path.suffixes))
        match = cls.VOICE_NAME_REGEX.match(voice_name)
        if match is None:
            raise ValueError(f"Invalid voice archive: `{archive_path}`")
        info = match.groupdict()
        language = info["language"]
        name = info["name"]
        quality = info["quality"]
        voice_key = f"voice-{language}-{name}-{quality}"
        with tarfile.open(os.fspath(archive_path), "r:gz") as tar:
            members = tar.getmembers()
            try:
                m_onnx_model = next(m for m in members if m.name.endswith(".onnx"))
                m_model_config = next(
                    m for m in members if m.name.endswith(".onnx.json")
                )
            except StopIteration:
                raise ValueError(f"Invalid voice archive: `{archive_path}`")
            dst = Path(dest_dir).joinpath(voice_key)
            dst.mkdir(parents=True, exist_ok=True)
            tar.extract(m_onnx_model, path=os.fspath(dst), set_attrs=False)
            tar.extract(m_model_config, path=os.fspath(dst), set_attrs=False)
            try:
                m_model_card = next(m for m in members if m.name.endswith("MODEL_CARD"))
            except StopIteration:
                pass
            else:
                tar.extract(m_model_card, path=os.fspath(dst), set_attrs=False)
            return voice_key


@dataclass
class PiperConfig:
    num_symbols: int
    num_speakers: int
    sample_rate: int
    espeak_voice: str
    length_scale: float
    noise_scale: float
    noise_w: float
    phoneme_id_map: Mapping[str, Sequence[int]]
    speaker_id_map: Mapping[str, int]

    @classmethod
    def load_from_json_file(cls, config_path: Union[str, Path]):
        with open(config_path, "r", encoding="utf-8") as config_file:
            config_dict = json.load(config_file)
            inference = config_dict.get("inference", {})

            return cls(
                num_symbols=config_dict["num_symbols"],
                num_speakers=config_dict["num_speakers"],
                sample_rate=config_dict["audio"]["sample_rate"],
                espeak_voice=config_dict["espeak"]["voice"],
                noise_scale=inference.get("noise_scale", 0.667),
                length_scale=inference.get("length_scale", 1.0),
                noise_w=inference.get("noise_w", 0.8),
                phoneme_id_map=config_dict["phoneme_id_map"],
                speaker_id_map=config_dict["speaker_id_map"],
            )

