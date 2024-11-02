import os.path
import subprocess

from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QSystemTrayIcon, QMenu, QTableWidgetItem,
                             QHeaderView, QFileDialog, QProgressBar, QLabel, QToolButton, QComboBox)
from PyQt6.QtGui import QIcon, QAction, QPixmap, QImage
from PyQt6.QtCore import Qt, QUrl, QPoint, pyqtSignal
from PyQt6 import uic
from PyQt6.QtWebEngineWidgets import QWebEngineView

from app_data import directory_to_save, updateSettings, tray_option, ffmpeg_path

from hotkeys import HotkeyThread

from main_window import Ui_MainWindow
from about import Ui_Form as About_Ui
from loading_confirm import Ui_Form as Loading_Confirm_Ui
from settings import Ui_Form as Settings_Ui
from quick_search import Ui_Form as Quick_Search_Ui

from network_tools import load_image_from_url


class MainWindow(QMainWindow, Ui_MainWindow):
    create_about_action = pyqtSignal()
    create_settings_action = pyqtSignal()
    create_loading_confirm_action = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.setBrowseMenu()
        self.setMoreMenu()
        self.setupButtons()
        self.setupBrowser()
        self.updateVideosList()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.searchButton.clicked.connect(
            lambda: self.create_loading_confirm_action.emit(self.lineEdit.text()))  # кнопка загрузки

        self.old_pos = self.pos()
        self.is_mouse_pressed = False

    def updateVideosList(self) -> None:
        self.videosList.setColumnCount(4)
        # self.videosList.setRowCount(1)

        self.videosList.setHorizontalHeaderLabels(["", "Название", "Статус", ""])
        self.videosList.setColumnWidth(0, 64)
        self.videosList.setColumnWidth(1, 110)
        self.videosList.setColumnWidth(2, 52)
        self.videosList.setColumnWidth(3, 42)

    def addVideoToTable(self, video_info) -> None:
        try:
            self.videosList.setRowCount(self.videosList.rowCount() + 1)
            last_elem = self.videosList.rowCount() - 1

            label = QLabel()
            label.setPixmap(video_info["thumbnail"])
            label.setScaledContents(True)

            button = QToolButton()
            button.setIcon(QIcon("icons/directory.png"))
            button.clicked.connect(lambda: subprocess.Popen(["explorer", directory_to_save]))
            print(video_info["directory"])

            self.videosList.setItem(last_elem, 1, QTableWidgetItem(video_info.get("title", "")))
            self.videosList.setCellWidget(last_elem, 2, QProgressBar())
            self.videosList.setCellWidget(last_elem, 3, button)
            self.videosList.setCellWidget(last_elem, 0, label)
        except Exception as e:
            print(e)

    def setupBrowser(self) -> None:
        self.webView = QWebEngineView()
        self.webView.urlChanged.connect(lambda: self.lineEdit.setText(self.webView.url().toString()))
        self.refreshButton.clicked.connect(self.webView.reload)
        self.backButton.clicked.connect(self.webView.back)
        self.backButton.clicked.connect(self.webView.forward)
        self.browseButton_2.clicked.connect(lambda: self.webView.setUrl(QUrl(self.lineEdit.text())))
        self.webBrowserHandler.addWidget(self.webView)
        self.webView.setUrl(QUrl.fromLocalFile("/index.html"))

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False

    def setBrowseMenu(self) -> None:
        self.browseMenu = QMenu()

        self.browseMenu.setStyleSheet("""QMenu {
        background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), 
        stop:1 rgba(239, 239, 239, 255));
        border: 1px solid #C1C1C1;
    }
    QMenu::item {
        padding: 5px 20px;
        alignment: center;
    }
    QMenu::item:selected {
        background-color: #0E9594;
        color: white;
    }""")
        self.browseButton.clicked.connect(self.openBrowseMenu)

        yt_action = QAction("Youtube", self)
        yt_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://www.youtube.com/")))
        self.browseMenu.addAction(yt_action)

        vk_action = QAction("VK Видео", self)
        vk_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://vk.com/video")))
        self.browseMenu.addAction(vk_action)

        dz_action = QAction("Дзен", self)
        dz_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://dzen.ru/")))
        self.browseMenu.addAction(dz_action)

        rt_action = QAction("Rutube", self)
        rt_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://rutube.ru/")))
        self.browseMenu.addAction(rt_action)

        sc_action = QAction("SoundCloud", self)
        sc_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://soundcloud.com/")))
        self.browseMenu.addAction(sc_action)

    def setMoreMenu(self) -> None:
        self.more_menu = QMenu()

        self.more_menu.setStyleSheet("""QMenu {
        background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), 
        stop:1 rgba(239, 239, 239, 255));
        border: 1px solid #C1C1C1;
    }
    QMenu::item {
        padding: 5px 20px;
        alignment: center;
    }
    QMenu::item:selected {
        background-color: #0E9594;
        color: white;
    }""")
        self.MoreButton.clicked.connect(self.openMoreMenu)

        capsule_action = QAction("Капсула времени", self)
        capsule_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://www.youtube.com/")))
        self.more_menu.addAction(capsule_action)

        multiload_action = QAction("Множ. загрузка", self)
        multiload_action.triggered.connect(lambda: self.webView.setUrl(QUrl("https://www.youtube.com/")))
        self.more_menu.addAction(multiload_action)

        settings_action = QAction("Настройки", self)
        settings_action.triggered.connect(lambda: self.create_settings_action.emit())
        self.more_menu.addAction(settings_action)

        about_action = QAction("О программе", self)
        about_action.triggered.connect(lambda: self.create_about_action.emit())
        self.more_menu.addAction(about_action)

    def openBrowseMenu(self) -> None:
        self.browseMenu.exec(self.browseButton.mapToGlobal(self.browseButton.rect().bottomLeft()))

    def openMoreMenu(self) -> None:
        self.more_menu.exec(self.MoreButton.mapToGlobal(self.MoreButton.rect().bottomLeft()))

    def setupButtons(self) -> None:
        self.CloseButton.clicked.connect(lambda: self.hide())
        self.HideButton.clicked.connect(lambda: self.showMinimized())


class AboutWindow(QWidget, About_Ui):
    def __init__(self):
        super().__init__()
        # uic.loadUi("about.ui", self)
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False


class SettingsWindow(QWidget, Settings_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupTrayComboBox()
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.savePath.setText(directory_to_save)
        self.FFmpegPath.setText(ffmpeg_path)
        self.trayComboBox.setCurrentIndex(tray_option)
        self.editButton.clicked.connect(self.editPath)
        self.editButton2.clicked.connect(self.editFFmpegPath)
        self.applyButton.clicked.connect(self.applySettings)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def setupTrayComboBox(self) -> None:
        self.trayComboBox.addItems(["Сворачивать в трей", "Закрывать"])

    def editPath(self) -> None:
        global directory_to_save
        directory_to_save = QFileDialog.getExistingDirectory()
        self.savePath.setText(directory_to_save)

    def editFFmpegPath(self) -> None:
        global ffmpeg_path
        ffmpeg_path = QFileDialog.getOpenFileName()
        self.FFmpegPath.setText(ffmpeg_path)

    def applySettings(self):
        updateSettings((self.savePath.text(), self.trayComboBox.currentIndex()))

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False


class ConfirmWindow(QWidget, Loading_Confirm_Ui):
    download_action = pyqtSignal(dict)

    def __init__(self, video_info, video_format):
        super().__init__()
        self.setupUi(self)

        self.video_info = video_info
        self.video_format = video_format

        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())

        self.downloadButton.clicked.connect(self.download_file)

        self.initInfo()

    def download_file(self):
        video_info = dict()
        video_info["title"] = self.video_info.get("title", "Не удалось получить название")
        video_info["thumbnail"] = load_image_from_url(self.video_info.get("thumbnail", ""))
        video_info["directory"] = directory_to_save
        video_info["url"] = self.video_info.get("original_url", "")
        video_info["format"] = self.formatBox.currentText()[:-1]
        video_info["ext"] = self.extensionBox.currentText()
        self.download_action.emit(video_info)

    def initInfo(self):
        self.fileName.setText(self.video_info.get("title", "Не удалось получить название"))
        self.formatText.setText(f"{self.formatText.text()} {self.video_info.get("ext", "Неизвестно")}")
        self.durationText.setText(f"{self.durationText.text()} {self.video_info.get("duration_string", "Неизвестно")}")

        if self.video_format["is_video"]:
            for f in reversed(sorted(self.video_format["formats"])):
                self.formatBox.addItem(f"{f}p")
        else:
            self.formatBox.addItem("Только аудио")

        for extension in sorted(self.video_format["extensions"]):
            self.extensionBox.addItem(extension)

        self.savePath.setText(f"{self.savePath.text()} {directory_to_save}")

        try:
            self.preview.setPixmap(load_image_from_url(self.video_info["thumbnail"]))
        except Exception as e:
            print(e)

    def mousePressEvent(self, a0) -> None:
        self.old_pos = a0.globalPosition().toPoint()
        self.is_mouse_pressed = True

    def mouseMoveEvent(self, a0) -> None:
        if self.is_mouse_pressed:
            delta = QPoint(a0.globalPosition().toPoint() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = a0.globalPosition().toPoint()

    def mouseReleaseEvent(self, a0) -> None:
        self.is_mouse_pressed = False


class QuickSearch(QWidget, Quick_Search_Ui):
    create_loading_confirm_action = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.closeButton.clicked.connect(lambda: self.hide())

        self.hide_hotkey = HotkeyThread("esc")
        self.hide_hotkey.hotkey_triggered.connect(lambda: self.closeQuickSearch)
        self.hide_hotkey.start()

        self.search_hotkey = HotkeyThread("enter")
        self.search_hotkey.hotkey_triggered.connect(self.search)
        self.search_hotkey.start()

    def closeQuickSearch(self):
        self.lineEdit.setText("")
        self.hide()

    def search(self):
        self.create_loading_confirm_action.emit(self.lineEdit.text())
        self.closeQuickSearch()
