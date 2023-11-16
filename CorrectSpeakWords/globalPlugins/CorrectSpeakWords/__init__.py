import globalPluginHandler
import string
import speech
import logging
import os

class CorrectSpeakWordsAddon(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super().__init__()

        # Configure o sistema de logging
        self.setup_logging()

        # Variável para armazenar a palavra em construção
        self.current_word = ""

        # Lista de caracteres de pontuação, incluindo espaço
        self.punctuation = string.punctuation + " "

        # Vincule o evento de digitação (keyTyped) ao manipulador de eventos
        self.key_event = self.key_event_handler

    def setup_logging(self):
        # Configuração do sistema de logging
        log_path = os.path.join(os.path.expanduser("~"), "Desktop", "addon_log.txt")
        logging.basicConfig(filename=log_path, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

    def terminate(self):
        # Quando o addon é encerrado, finalize qualquer pronúncia pendente
        self.speakAndClearWord()

    def speakAndClearWord(self):
        # Verifica se há uma palavra em construção para pronunciar e limpa a variável
        if self.current_word:
            speech.cancelSpeech()  # Cancela a pronúncia pendente
            speech.speak(self.current_word)  # Pronuncia a palavra construída
            self.log_event("Word spoken: " + self.current_word)
            self.current_word = ""  # Limpa a palavra em construção

    def process_key_event(self, key):
        # Processa a tecla pressionada
        if key == "\b":
            # Se a tecla é um backspace, remove o último caractere da palavra em construção
            self.log_event("Backspace pressed")
            self.current_word = self.current_word[:-1]
        elif key in self.punctuation:
            # Se a tecla é uma pontuação, pronuncia a palavra construída e limpa
            self.speakAndClearWord()
        else:
            # Caso contrário, adiciona o caractere à palavra em construção
            self.current_word += key

    def key_event_handler(self, gesture):
        # Manipulador de eventos para teclas pressionadas
        key = gesture.text
        self.log_event("Key pressed: " + key)
        self.process_key_event(key)

    def log_event(self, message):
        # Função para registrar eventos no arquivo de log
        logging.info(message)

# Instancia o addon quando o NVDA é inicializado
addon = CorrectSpeakWordsAddon()
