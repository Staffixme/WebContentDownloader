import time

from yt_dlp import YoutubeDL
from PyQt6.QtCore import QRunnable, pyqtSlot

from app_data import ffmpeg_path

from os import path


class Downloader(QRunnable):
    def __init__(self, video_info):
        super().__init__()
        self.video_info = video_info

    @pyqtSlot()
    def run(self):
        ydl_opts = {
            'outtmpl': path.join(self.video_info.get("directory", ""), self.video_info.get("title", "")),
            'ffmpeg_location': ffmpeg_path,
            'format': f"bestvideo[height<={self.video_info["format"]}]+bestaudio/best[height<={self.video_info["format"]}]",
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': self.video_info["ext"],
            }],
            'socket_timeout': 50,
            'retry_scale': 5,
            'retries': 15,
            'noplaylist': True,
            # 'sponsorblock': self.is_ad_delete,
            # 'sponsorblock-remove': ['sponsor'],
        }

        while True:
            try:
                with YoutubeDL(ydl_opts) as downloader:
                    downloader.download(self.video_info.get("url", ""))
                break
            except OSError as e:
                if e.errno == 32:
                    print("Процесс все еще занят.")
                    time.sleep(5)
            else:
                raise Exception("can't download")
