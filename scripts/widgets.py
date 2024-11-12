import os
from os import path, startfile

from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow, QSystemTrayIcon, QMenu, QTableWidgetItem,
                             QHeaderView, QFileDialog, QProgressBar, QLabel, QToolButton, QComboBox, QMessageBox)
from PyQt6.QtGui import QIcon, QAction, QPixmap, QImage
from PyQt6.QtCore import Qt, QUrl, QPoint, pyqtSignal, pyqtSlot
from PyQt6 import uic
from PyQt6.QtWebEngineWidgets import QWebEngineView

from app_data import directory_to_save, update_settings, tray_option, ffmpeg_path, APP_VERSION, add_video_to_database, \
    video_list

from webbrowser import open

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
        self.check_ffmpeg()
        self.set_browse_menu()
        self.set_more_menu()
        self.setup_buttons()
        self.setup_browser()
        self.update_videos_list()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.download_button.clicked.connect(
            lambda: self.create_loading_confirm_action.emit(self.lineEdit.text()))  # кнопка загрузки

        self.old_pos = self.pos()
        self.is_mouse_pressed = False

    def check_ffmpeg(self):
        if not ffmpeg_path:
            message = QMessageBox(self,
                                  "FFmpeg не найден.\nДля правильной работы программы нужен FFmpeg. Если он установлен,"
                                  " то укажите путь в настройках. Если FFmpeg не установлен, то вы можете установить"
                                  " его с официального сайта ffmpeg.org")
            message_exec = message.exec()

    def update_videos_list(self) -> None:
        self.videosList.setColumnCount(4)

        self.videosList.setHorizontalHeaderLabels(["", "Название", "Статус", ""])
        self.videosList.setColumnWidth(0, 48)
        self.videosList.setColumnWidth(1, 107)
        self.videosList.setColumnWidth(2, 50)

        global video_list
        for i in range(len(video_list)):
            self.videosList.setRowCount(self.videosList.rowCount() + 1)
            last_elem = self.videosList.rowCount() - 1
            label = QLabel()
            label.setPixmap(QPixmap(video_list[i][2]))
            label.setScaledContents(True)
            button = QToolButton()
            button.setIcon(QIcon("../icons/directory.png"))
            button.clicked.connect(lambda: startfile(directory_to_save))
            complete_icon = QLabel()
            complete_icon.setPixmap(QPixmap("../icons/completed.png"))

            self.videosList.setItem(last_elem, 1, QTableWidgetItem(video_list[i][1]))
            self.videosList.setCellWidget(last_elem, 2, complete_icon)
            self.videosList.setCellWidget(last_elem, 3, button)
            self.videosList.setCellWidget(last_elem, 0, label)

    def add_video_to_table(self, video) -> None:
        try:
            video_info = video.video_info

            self.videosList.setRowCount(self.videosList.rowCount() + 1)
            last_elem = self.videosList.rowCount() - 1

            label = QLabel()
            label.setPixmap(video_info["thumbnail"])
            label.setScaledContents(True)

            button = QToolButton()
            button.setIcon(QIcon("../icons/directory.png"))
            button.clicked.connect(lambda: startfile(directory_to_save))

            progress = QProgressBar()
            video.downloader.signal.update_loading_progress.connect(lambda x: progress.setValue(x))

            self.videosList.setItem(last_elem, 1, QTableWidgetItem(video_info.get("title", "")))
            self.videosList.setCellWidget(last_elem, 2, progress)
            self.videosList.setCellWidget(last_elem, 3, button)
            self.videosList.setCellWidget(last_elem, 0, label)

            add_video_to_database(video_info.get("title", ""), video_info.get("thumbnail_path", ""))
        except Exception as e:
            print(f"cannot add video to table: {e}")

    def setup_browser(self) -> None:
        self.webView = QWebEngineView()
        self.webView.urlChanged.connect(self.change_url_text)
        self.webView.loadProgress.connect(self.progressbar_update)
        self.webView.loadStarted.connect(self.progressbar_start)
        self.webView.loadFinished.connect(self.progressbar_finish)
        self.refreshButton.clicked.connect(self.webView.reload)
        self.backButton.clicked.connect(self.webView.back)
        self.backButton.clicked.connect(self.webView.forward)
        self.search_button.clicked.connect(lambda: self.webView.setUrl(QUrl(self.lineEdit.text())))
        self.webBrowserHandler.addWidget(self.webView)
        self.webView.setUrl(QUrl.fromLocalFile(f"/index.html"))

    def change_url_text(self):
        self.lineEdit.setText(self.webView.url().toString())

    @pyqtSlot(int)
    def progressbar_update(self, progress):
        self.progressBar.setValue(progress)

    @pyqtSlot()
    def progressbar_start(self):
        self.progressBar.show()
        self.pageName.setText("Загрузка страницы...")

    @pyqtSlot()
    def progressbar_finish(self):
        self.pageName.setText(str(self.webView.title()))
        self.progressBar.hide()

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

    def set_browse_menu(self) -> None:
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
        self.browseButton.clicked.connect(self.open_browse_menu)

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

    def set_more_menu(self) -> None:
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
        self.MoreButton.clicked.connect(self.open_more_menu)

        settings_action = QAction("Настройки", self)
        settings_action.triggered.connect(lambda: self.create_settings_action.emit())
        self.more_menu.addAction(settings_action)

        about_action = QAction("О программе", self)
        about_action.triggered.connect(lambda: self.create_about_action.emit())
        self.more_menu.addAction(about_action)

    def open_browse_menu(self) -> None:
        self.browseMenu.exec(self.browseButton.mapToGlobal(self.browseButton.rect().bottomLeft()))

    def open_more_menu(self) -> None:
        self.more_menu.exec(self.MoreButton.mapToGlobal(self.MoreButton.rect().bottomLeft()))

    def setup_buttons(self) -> None:
        self.CloseButton.clicked.connect(self.close_app)
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def close_app(self):
        global tray_option
        if tray_option == 0:
            self.hide()
        elif tray_option == 1:
            self.close()


class AboutWindow(QWidget, About_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.version.setText(f"{self.version.text()} {APP_VERSION}")

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())
        self.updateButton.clicked.connect(lambda: open("https://github.com/Staffixme/WebContentDownloader"))

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
        self.setup_tray_combo_box()
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.savePath.setText(directory_to_save)
        self.FFmpegPath.setText(ffmpeg_path)
        self.trayComboBox.setCurrentIndex(tray_option)
        self.editButton.clicked.connect(self.edit_path)
        self.editButton2.clicked.connect(self.edit_ffmpeg_path)
        self.applyButton.clicked.connect(self.apply_settings)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def setup_tray_combo_box(self) -> None:
        self.trayComboBox.addItems(["Сворачивать в трей", "Закрывать"])

    def edit_path(self) -> None:
        global directory_to_save
        directory_to_save = QFileDialog.getExistingDirectory()
        self.savePath.setText(directory_to_save)

    def edit_ffmpeg_path(self) -> None:
        global ffmpeg_path
        ffmpeg_path = QFileDialog.getOpenFileName()[0]
        self.FFmpegPath.setText(ffmpeg_path)

    def apply_settings(self):
        update_settings((self.savePath.text(), self.trayComboBox.currentIndex(), self.FFmpegPath.text()))

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

        self.init_info()

    def download_file(self):
        video_info = dict()
        video_info["title"] = self.fileName.text()
        thumbnail = load_image_from_url(self.video_info.get("thumbnail", ""))
        thumbnail.save(
            f"../WebContent App/Thumbnails/{self.video_info.get("title", "Не удалось получить название")}.jpg",
            "JPG")
        video_info["thumbnail"] = thumbnail
        video_info["thumbnail_path"] = (f"../WebContent App/Thumbnails/"
                                        f"{self.video_info.get("title", "Не удалось получить название")}.jpg")
        video_info["directory"] = directory_to_save
        video_info["url"] = self.video_info.get("original_url", "")
        video_info["format"] = self.formatBox.currentText()[:-1]
        video_info["ext"] = self.extensionBox.currentText()
        video_info["is_sponsorblock"] = self.sponsorBlockBox.isChecked()
        self.download_action.emit(video_info)

    def init_info(self):
        self.fileName.setText(self.video_info.get("title", "Не удалось получить название"))
        self.formatText.setText(f"{self.formatText.text()} {self.video_info.get("ext", "Неизвестно")}")
        self.durationText.setText(f"{self.durationText.text()} {self.video_info.get("duration_string", "Неизвестно")}")

        if self.video_format["is_video"]:
            for f in reversed(sorted(self.video_format["formats"])):
                self.formatBox.addItem(f"{f}p")
            for extension in ("mp4", "mov", "mkv", "m4v", "avi", "flv", "m2ts"):
                self.extensionBox.addItem(extension)
        elif not self.video_format["is_video"]:
            for extension in ("mp3",):
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
        self.searchButton.clicked.connect(self.search)

    def close_quick_search(self):
        self.lineEdit.setText("")
        self.hide()

    def search(self):
        self.create_loading_confirm_action.emit(self.lineEdit.text())
        self.close_quick_search()
