import sys

from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QSplashScreen
from PyQt6.QtGui import QIcon, QAction, QPixmap, QColor
from PyQt6.QtCore import Qt, QThreadPool
from widgets import MainWindow, AboutWindow, SettingsWindow, ConfirmWindow, QuickSearch

from hotkeys import HotkeyThread
from network_tools import get_video_info
from video import Video

if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)


class AppManager:
    def __init__(self):
        super().__init__()
        self.create_tray()

        splash_screen = QSplashScreen(QPixmap("../icons/splash_screen2.png"))
        splash_screen.show()
        splash_screen.showMessage("Загрузка...", color=QColor("white"))
        self.quick_search = QuickSearch()
        self.quicksearch_hotkey = HotkeyThread("ctrl+q")
        self.quicksearch_hotkey.hotkey_triggered.connect(self.open_quick_search)
        self.quicksearch_hotkey.start()
        self.quick_search.create_loading_confirm_action.connect(self.open_confirm_window)
        self.thread_pool = QThreadPool.globalInstance()

        self.main_window = MainWindow()
        self.main_window.show()

        self.main_window.create_about_action.connect(self.open_about_window)
        self.main_window.create_settings_action.connect(self.open_settings_window)
        self.main_window.create_loading_confirm_action.connect(self.open_confirm_window)

    def create_tray(self):
        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon("../icons/downloader_icon_clear.png"))
        self.tray_icon.setVisible(True)

        self.tray_menu = QMenu()
        self.tray_menu.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.tray_menu.setStyleSheet("""QMenu {
        background-color: rgb(255, 255, 255);
        border: 1px solid #C1C1C1;
        border-radius: 5px;
        }
        QMenu::item {
            padding: 5px 20px;
            alignment: center;
            border-radius: 5px;
        }
        QMenu::item:selected {
            background-color: #0E9594;
            color: white;
        }""")

        self.open_action = QAction("Открыть")
        self.open_action.triggered.connect(lambda: self.main_window.show())
        self.tray_icon.activated.connect(lambda: self.main_window.show())
        self.tray_menu.addAction(self.open_action)

        self.f_action = QAction("Свернуть")
        self.f_action.triggered.connect(lambda: self.main_window.hide())
        self.tray_menu.addAction(self.f_action)

        self.exit_action = QAction("Выйти")
        self.exit_action.triggered.connect(lambda: QApplication.quit())
        self.tray_menu.addAction(self.exit_action)

        self.tray_icon.setContextMenu(self.tray_menu)
        self.tray_icon.setToolTip("WebContent Downloader")

    def open_about_window(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def open_settings_window(self):
        self.settings_window = SettingsWindow()
        self.settings_window.show()

    def open_confirm_window(self, url: str):
        if self.main_window.isHidden():
            self.main_window.show()

        try:
            video_info = get_video_info(url)
            self.loading_confirm_window = ConfirmWindow(*video_info)
            self.loading_confirm_window.download_action.connect(self.add_video_to_thread)
            self.loading_confirm_window.show()
        except Exception as e:
            print(f"AppManager - cannot open loading confirm window: {e}")

    def add_video_to_thread(self, video_info):
        try:
            video = Video(video_info)
            self.main_window.add_video_to_table(video)
            self.thread_pool.start(video.downloader)
        except Exception as e:
            print(f"AppManager - cannot add video to thread: {e}")

    def open_quick_search(self):
        self.quick_search.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    appManager = AppManager()
    sys.exit(app.exec())
