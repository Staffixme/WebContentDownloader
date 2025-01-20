from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import pyqtSlot, QUrl
from network_tools import load_image_from_url


class WebPageTab(QWidget):
    def __init__(self, url_line):
        super().__init__()

        self.url_line = url_line

        self.layout = QVBoxLayout()
        self.webview = QWebEngineView()
        self.progress_bar = QProgressBar()

        self.progress_bar.setFixedHeight(3)
        self.progress_bar.setStyleSheet("""
        .QProgressBar{
            background-color: #D2D2D2;
            border-radius: 5px;
        }
        
        .QProgressBar:chunk{
            background-color: #0E9594;
        }
        """)

        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.progress_bar)
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)

        self.webview.loadProgress.connect(self.progressbar_update)
        self.webview.loadStarted.connect(self.progressbar_start)
        self.webview.loadFinished.connect(self.progressbar_finish)
        self.webview.iconUrlChanged.connect(lambda icon: self.change_icon(icon))
        self.webview.titleChanged.connect(lambda title: self.change_title(title))
        self.webview.urlChanged.connect(lambda url: self.change_url(url))

    def load_page(self, url):
        self.webview.setUrl(QUrl(url))

    @pyqtSlot(int)
    def progressbar_update(self, progress):
        self.progress_bar.setValue(progress)

    def progressbar_start(self):
        self.progress_bar.show()
        self.parent().parent().setTabText(self.parent().parent().indexOf(self), "Загрузка...")

    def progressbar_finish(self):

        self.progress_bar.hide()

    def change_icon(self, icon):
        if icon.isValid():
            self.parent().parent().setTabIcon(self.parent().parent().indexOf(self),
                                              QIcon(load_image_from_url(icon.toString())))
        else:
            print("url is not valid")

    def change_title(self, title):
        if len(title) >= 12:
            title = self.webview.title()[:11] + "..."

        self.parent().parent().setTabText(self.parent().parent().indexOf(self), title)

    def change_url(self, url):
        if self.parent():
            if self.parent().parent().currentIndex() == self.parent().parent().indexOf(self):
                self.url_line.setText(url.toString())
