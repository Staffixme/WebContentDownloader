import requests
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QByteArray

import yt_dlp


def get_video_info(url: str) -> tuple:
    with yt_dlp.YoutubeDL() as viewer:
        video_info = viewer.extract_info(url, download=False)

    video_format = dict()

    if 'acodec' in video_info and video_info['acodec'] != 'none':
        video_format["is_video"] = False
    else:
        video_format["is_video"] = True

    extensions = {fmt['ext'] for fmt in video_info.get('formats', [])}
    video_format["extensions"] = extensions

    formats = set()
    allowed_formats = {"144", "240", "360", "480", "720", "1080", "1440", "2160"}

    for f in video_info["formats"]:
        quality = f.get('height', '')
        if quality and str(quality) in allowed_formats:
            formats.add(str(quality))

    video_format["formats"] = formats

    return video_info, video_format


def load_image_from_url(url) -> QPixmap:
    if url:
        response = requests.get(url)
        if response.status_code == 200:
            pixmap = QPixmap()
            pixmap.loadFromData(QByteArray(response.content))
            return pixmap
        else:
            print("Ошибка загрузки изображения:", response.status_code)
            return QPixmap("../icons/unknown_preview.png")
    else:
        return QPixmap("../icons/unknown_preview.png")
