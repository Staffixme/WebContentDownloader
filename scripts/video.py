from content_downloader import Downloader
from PyQt6.QtCore import pyqtSignal


class Video:
    progress = pyqtSignal(int)

    def __init__(self, video_info):
        self.video_info = video_info
        self.downloader = Downloader(self.video_info)
