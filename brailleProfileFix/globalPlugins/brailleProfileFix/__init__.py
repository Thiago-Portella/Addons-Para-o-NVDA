import globalPluginHandler
import braille
from logHandler import log

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    """
    Plugin global para prevenir a desconexão indevida da linha braille 
    durante a alternância de perfis de configuração do NVDA.
    """

    VIRTUAL_DRIVERS = ("noBraille", "auto")

    def __init__(self):
        super().__init__()
        self._patched = False
        self._apply_patches()

    def _apply_patches(self):
        if not hasattr(braille, "handler"):
            log.error("BrailleProfileFix: Instância braille.handler não encontrada. Patch abortado.")
            return

        # Armazena as referências originais dos métodos
        self.orig_setDisplayByName = braille.handler.setDisplayByName
        self.orig_setDisplay = braille.handler._setDisplay

        # Aplica o monkey patching na instância ativa
        braille.handler.setDisplayByName = self._patched_setDisplayByName
        braille.handler._setDisplay = self._patched_setDisplay
        
        self._patched = True
        log.info("BrailleProfileFix: Hooks aplicados com sucesso em braille.handler.")

    def _get_current_driver(self):
        """Retorna o nome do driver de hardware atualmente em uso."""
        return getattr(braille.handler.display, "name", "noBraille")

    def _should_block_transition(self, target_driver):
        """Avalia se a transição de driver deve ser interceptada."""
        current_driver = self._get_current_driver()
        
        # Permite qualquer transição se não houver hardware físico ativo
        if current_driver in self.VIRTUAL_DRIVERS:
            return False

        # Bloqueia transições para estados virtuais ou recarregamentos redundantes
        if target_driver in self.VIRTUAL_DRIVERS or target_driver == current_driver:
            log.debug(f"BrailleProfileFix: Transição interceptada ({current_driver} -> {target_driver}). Porta mantida.")
            return True

        return False

    def _patched_setDisplayByName(self, *args, **kwargs):
        """Wrapper para o método setDisplayByName."""
        try:
            target_driver = args[0] if args else kwargs.get("name")
            if self._should_block_transition(target_driver):
                return True
        except Exception as e:
            log.error(f"BrailleProfileFix: Erro no hook setDisplayByName: {e}")

        return self.orig_setDisplayByName(*args, **kwargs)

    def _patched_setDisplay(self, *args, **kwargs):
        """Wrapper para o método interno _setDisplay."""
        try:
            target_driver = args[0] if args else kwargs.get("driverName")
            if self._should_block_transition(target_driver):
                return None
        except Exception as e:
            log.error(f"BrailleProfileFix: Erro no hook _setDisplay: {e}")

        return self.orig_setDisplay(*args, **kwargs)

    def terminate(self):
        """Remove as interceptações e restaura o estado original ao descarregar o plugin."""
        if self._patched:
            braille.handler.setDisplayByName = self.orig_setDisplayByName
            braille.handler._setDisplay = self.orig_setDisplay
            log.info("BrailleProfileFix: Hooks removidos com sucesso.")
        super().terminate()