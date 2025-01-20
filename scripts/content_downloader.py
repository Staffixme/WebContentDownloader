import time

from yt_dlp import YoutubeDL
from PyQt6.QtCore import QRunnable, pyqtSlot, pyqtSignal, QObject

import app_data

from os import path


class DownloaderSignals(QObject):
    update_loading_progress = pyqtSignal(int)
    ffmpeg_error = pyqtSignal()


class Downloader(QRunnable):
    def __init__(self, video_info):
        super().__init__()
        self.video_info = video_info
        self.signal = DownloaderSignals()

    @pyqtSlot()
    def run(self):
        if self.video_info["format"] == "Только аудио":
            format = "bestaudio"
            extension = "mp3"
        else:
            format = f"bestvideo[height<={self.video_info["format"][:-1]}]+bestaudio/best[height<={self.video_info["format"][:-1]}]"
            extension = self.video_info["ext"]
        ydl_opts = {
            'outtmpl': path.join(self.video_info.get("directory", ""), self.video_info.get("title", "")),
            'ffmpeg_location': app_data.ffmpeg_path,
            'progress_hooks': [self.return_loading_progress],
            'format': format,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': extension,
            }],
            'socket_timeout': 50,
            'retry_scale': 5,
            'retries': 15,
            'noplaylist': True,
            'sponsorblock': self.video_info.get("is_sponsorblock", False),
            'sponsorblock-remove': ['sponsor'],
        }
        try:
            while True:
                try:
                    with YoutubeDL(ydl_opts) as downloader:
                        downloader.download(self.video_info.get("url", ""))
                    break
                except OSError as e:
                    if e.errno == 32:
                        print("Процесс все еще занят.")
                        time.sleep(5)
        except Exception:
            self.signal.ffmpeg_error.emit()

    def return_loading_progress(self, value):
        if value['status'] == 'downloading':
            downloaded = value.get('downloaded_bytes', 0)
            total = value.get('total_bytes', None)

            if total is not None and total > 0:
                progress = (downloaded / total) * 100
            else:
                progress = 0

            self.signal.update_loading_progress.emit(int(progress))
