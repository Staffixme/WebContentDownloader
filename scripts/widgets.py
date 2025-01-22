from os import startfile

from PyQt6.QtWidgets import (QWidget, QMainWindow, QMenu, QTableWidgetItem,
                             QFileDialog, QProgressBar, QLabel, QToolButton, QMessageBox, QPushButton, QHeaderView)
from PyQt6.QtGui import QIcon, QAction, QPixmap
from PyQt6.QtCore import Qt, QUrl, QPoint, pyqtSignal
from WebPage import WebPageTab

import app_data

from webbrowser import open

from main_window import Ui_MainWindow
from about import Ui_Form as About_Ui
from loading_confirm import Ui_Form as Loading_Confirm_Ui
from settings import Ui_Form as Settings_Ui
from quick_search import Ui_Form as Quick_Search_Ui

from network_tools import load_image_from_url
from path_to_files import PATH, PATH_TO_WEBPAGE


class MainWindow(QMainWindow, Ui_MainWindow):
    create_about_action = pyqtSignal()
    create_settings_action = pyqtSignal()
    create_loading_confirm_action = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.version_text.setText(f"v.{app_data.APP_VERSION}")
        self.check_ffmpeg()
        self.set_browse_menu()
        self.setup_menu()
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
        if not app_data.ffmpeg_path:
            message = QMessageBox.warning(self, "FFmpeg не найден",
                                          "FFmpeg не найден.\nДля правильной работы программы нужен FFmpeg. Если он установлен,"
                                          " то укажите путь в настройках. Если FFmpeg не установлен, то вы можете установить"
                                          " его с официального сайта ffmpeg.org")

    def ffmpeg_error_dialog(self):
        QMessageBox.warning(self, "Ошибка загрузки",
                            "Не удалось скачать файл. Это может быть связано с тем, что программа не смогла найти"
                            " FFmpeg по указанному пути, либо не удалось получить ответ от сервера."
                            " Укажите действительный путь к FFmpeg в настроках или повторите попытку.")

    def update_videos_list(self) -> None:
        self.videosList.setColumnCount(4)
        for i in range(4):
            self.videosList.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeMode.Fixed)

        self.videosList.setColumnWidth(0, 48)
        self.videosList.setColumnWidth(1, 89)
        self.videosList.setColumnWidth(2, 50)

        for i in range(len(app_data.video_list)):
            self.videosList.setRowCount(self.videosList.rowCount() + 1)
            last_elem = self.videosList.rowCount() - 1
            label = QLabel()
            label.setPixmap(QPixmap(app_data.video_list[i][2]))
            label.setScaledContents(True)
            button = QToolButton()
            button.setIcon(QIcon(f"{PATH}/directory.png"))
            button.setStyleSheet("""
                    .QToolButton{
                    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 
                    rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));
                    border: none;
                    }
                    
                    .QToolButton:hover{
                        background-color: rgba(0, 0, 0, 50);
                    }
                    """)
            button.clicked.connect(lambda: startfile(app_data.directory_to_save))
            complete_icon = QLabel()
            complete_icon.setPixmap(QPixmap(f"{PATH}/completed.png"))
            complete_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.videosList.setItem(last_elem, 1, QTableWidgetItem(app_data.video_list[i][1]))
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
            button.setIcon(QIcon(f"{PATH}/directory.png"))
            button.setStyleSheet("""
                                .QToolButton{
                                background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 
                                rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));
                                border: none;
                                }

                                .QToolButton:hover{
                                    background-color: rgba(0, 0, 0, 50);
                                }
                                """)
            button.clicked.connect(lambda: startfile(app_data.directory_to_save))

            progress = QProgressBar()
            video.downloader.signal.update_loading_progress.connect(lambda x: progress.setValue(x))

            self.videosList.setItem(last_elem, 1, QTableWidgetItem(video_info.get("title", "")))
            self.videosList.setCellWidget(last_elem, 2, progress)
            self.videosList.setCellWidget(last_elem, 3, button)
            self.videosList.setCellWidget(last_elem, 0, label)

            app_data.add_video_to_database(video_info.get("title", ""), video_info.get("thumbnail_path", ""))
        except Exception as e:
            print(f"cannot add video to table: {e}")

    def setup_browser(self) -> None:
        self.new_button = QPushButton()
        self.new_button.setStyleSheet("""
            width: 24px;
            height: 24px;
            background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), 
            stop:1 rgba(239, 239, 239, 255));
            border: 1px solid #C1C1C1;
        """)
        self.new_button.setIcon(QIcon(f"{PATH}/add.png"))
        self.refreshButton.clicked.connect(self.reload_page)
        self.backButton.clicked.connect(self.go_back)
        self.forwardButton.clicked.connect(self.go_forward)
        self.search_button.clicked.connect(self.search)
        self.new_button.clicked.connect(lambda: self.add_tab(QUrl.fromLocalFile(f"{PATH_TO_WEBPAGE}/index.html")))
        self.webBrowserHandler.setCornerWidget(self.new_button)
        self.webBrowserHandler.tabCloseRequested.connect(self.close_tab)
        self.webBrowserHandler.currentChanged.connect(self.change_url_text)

        self.add_tab(QUrl.fromLocalFile(f"{PATH_TO_WEBPAGE}/index.html"))

    def add_tab(self, url):
        self.webView = WebPageTab(self.lineEdit)
        self.webView.load_page(url)

        self.webBrowserHandler.addTab(self.webView, QIcon(f"{PATH}/sitelogo.png"), None)
        self.webBrowserHandler.setCurrentWidget(self.webView)

    def close_tab(self, index):
        if self.webBrowserHandler.count() > 1:
            self.webBrowserHandler.removeTab(index)

    def go_back(self):
        current_tab = self.webBrowserHandler.currentWidget()
        if current_tab:
            current_tab.webview.back()

    def go_forward(self):
        current_tab = self.webBrowserHandler.currentWidget()
        if current_tab:
            current_tab.webview.forward()

    def reload_page(self):
        current_tab = self.webBrowserHandler.currentWidget()
        if current_tab:
            current_tab.webview.reload()

    def search(self):
        url = self.lineEdit.text()
        current_tab = self.webBrowserHandler.currentWidget()
        if current_tab:
            try:
                current_tab.load_page(url)
            except Exception as e:
                print(e)

    def change_url_text(self):
        self.lineEdit.setText(self.webBrowserHandler.currentWidget().webview.url().toString())

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

    def setup_menu(self):
        self.menu = QMenu()

        self.menu.setStyleSheet("""QMenu {
        background-color: rgb(255, 255, 255);
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
        self.menu_button.clicked.connect(self.open_settings_menu)

        settings_action = QAction("Настройки", self)
        settings_action.triggered.connect(lambda: self.create_settings_action.emit())
        self.menu.addAction(settings_action)

        about_action = QAction("О программе", self)
        about_action.triggered.connect(lambda: self.create_about_action.emit())
        self.menu.addAction(about_action)

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
        yt_action.triggered.connect(lambda: self.add_tab(QUrl("https://www.youtube.com/")))
        self.browseMenu.addAction(yt_action)

        vk_action = QAction("VK Видео", self)
        vk_action.triggered.connect(lambda: self.add_tab(QUrl("https://vk.com/video")))
        self.browseMenu.addAction(vk_action)

        dz_action = QAction("Дзен", self)
        dz_action.triggered.connect(lambda: self.add_tab(QUrl("https://dzen.ru/")))
        self.browseMenu.addAction(dz_action)

        rt_action = QAction("Rutube", self)
        rt_action.triggered.connect(lambda: self.add_tab(QUrl("https://rutube.ru/")))
        self.browseMenu.addAction(rt_action)

        sc_action = QAction("SoundCloud", self)
        sc_action.triggered.connect(lambda: self.add_tab(QUrl("https://soundcloud.com/")))
        self.browseMenu.addAction(sc_action)

    def open_browse_menu(self) -> None:
        self.browseMenu.exec(self.browseButton.mapToGlobal(self.browseButton.rect().bottomLeft()))

    def open_settings_menu(self) -> None:
        self.menu.exec(self.menu_button.mapToGlobal(self.menu_button.rect().bottomLeft()))

    def setup_buttons(self) -> None:
        self.CloseButton.clicked.connect(self.close_app)
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def close_app(self):
        if app_data.tray_option == 0:
            self.hide()
        elif app_data.tray_option == 1:
            self.close()


class AboutWindow(QWidget, About_Ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.old_pos = self.pos()
        self.is_mouse_pressed = False
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.version.setText(f"{self.version.text()} {app_data.APP_VERSION}")

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
        self.savePath.setText(app_data.directory_to_save)
        self.FFmpegPath.setText(app_data.ffmpeg_path)
        self.trayComboBox.setCurrentIndex(app_data.tray_option)
        self.editButton.clicked.connect(self.edit_path)
        self.editButton2.clicked.connect(self.edit_ffmpeg_path)
        self.applyButton.clicked.connect(self.apply_settings)

        self.CloseButton.clicked.connect(lambda: self.close())
        self.HideButton.clicked.connect(lambda: self.showMinimized())

    def setup_tray_combo_box(self) -> None:
        self.trayComboBox.addItems(["Сворачивать в трей", "Закрывать"])

    def edit_path(self) -> None:
        app_data.directory_to_save = QFileDialog.getExistingDirectory()
        self.savePath.setText(app_data.directory_to_save)

    def edit_ffmpeg_path(self) -> None:
        app_data.ffmpeg_path = QFileDialog.getOpenFileName()[0]
        self.FFmpegPath.setText(app_data.ffmpeg_path)

    def apply_settings(self):
        app_data.update_settings((self.savePath.text(), self.trayComboBox.currentIndex(), self.FFmpegPath.text()))

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
        self.formatBox.currentTextChanged.connect(lambda index: self.block_extension(index))
        self.init_info()

    def block_extension(self, index):
        if index == "Только аудио":
            self.extensionBox.setEnabled(False)
        else:
            self.extensionBox.setEnabled(True)

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
        video_info["directory"] = app_data.directory_to_save
        video_info["url"] = self.video_info.get("original_url", "")
        video_info["format"] = self.formatBox.currentText()
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
            self.formatBox.addItem("Только аудио")
            for extension in ("mp4", "mov", "mkv", "m4v", "avi", "flv", "m2ts"):
                self.extensionBox.addItem(extension)
        elif not self.video_format["is_video"]:
            self.formatBox.addItem("Только аудио")
            for extension in ("mp3",):
                self.extensionBox.addItem(extension)

        self.savePath.setText(f"{self.savePath.text()} {app_data.directory_to_save}")

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
