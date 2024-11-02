from PyQt6.QtCore import QThread, pyqtSignal
import keyboard


class HotkeyThread(QThread):
    hotkey_triggered = pyqtSignal()

    def __init__(self, combination: str):
        super().__init__()
        self.combination = combination

    def run(self):
        keyboard.add_hotkey(self.combination, self.trigger_hotkey)

    def trigger_hotkey(self):
        self.hotkey_triggered.emit()
