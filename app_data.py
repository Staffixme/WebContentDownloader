import sqlite3
import os
import string

# Информация о программе
APP_VERSION = "1.0"

# Настройки программы
tray_option = 0
directory_to_save = ""
user_login = ""
ffmpeg_path = ""

# Список сохраненных видео
video_list = list()


def findFFmpeg():
    drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]

    for drive in drives:
        for root, dirs, files in os.walk(drive):
            if "ffmpeg.exe" in files:
                return os.path.join(root, 'ffmpeg.exe')
    return ""


with sqlite3.connect("app_settings.sqlite") as db:
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS App_settings (
    Id                  INTEGER PRIMARY KEY AUTOINCREMENT
                                NOT NULL
                                UNIQUE,
    Directory_to_save TEXT,
    Hide_in_tray      INTEGER DEFAULT (0),
    Ffmpeg_path TEXT 
    );""")
    settings = cur.execute("""
    SELECT * FROM App_settings
    WHERE Id = 0
    """).fetchall()
    if not settings:
        cur.execute(f"""
        INSERT INTO App_settings(Id, Directory_to_save, Ffmpeg_path) VALUES(0, "", "{findFFmpeg()}")
        """)
        settings = cur.execute("""
            SELECT * FROM App_settings
            WHERE Id = 0
            """).fetchall()
    print(directory_to_save, tray_option, settings)
print(settings[0][1])
directory_to_save = settings[0][1]
tray_option = settings[0][2]
ffmpeg_path = settings[0][3]

if not os.path.isdir(os.path.join(os.getcwd(), "WebContent Downloader")):
    os.mkdir(os.path.join(os.getcwd(), "WebContent Downloader"))
    os.mkdir(os.path.join(os.getcwd(), "WebContent Downloader", "Thumbnails"))
    os.mkdir(os.path.join(os.getcwd(), "WebContent Downloader", "Local databases"))

with sqlite3.connect("WebContent Downloader/Local databases/videos.sqlite") as vdb:
    cur = vdb.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Videos (
    id        INTEGER PRIMARY KEY AUTOINCREMENT
                      NOT NULL
                      UNIQUE,
    title     TEXT    NOT NULL,
    thumbnail TEXT    NOT NULL
    );""")
    videos = cur.execute("""
    SELECT * FROM Videos
    """).fetchall()
    for i in range(len(videos)):
        print(i, i[0][1])
        video_list.append(videos[0][i])


def add_video_to_database(title: str, thumbanail: str):
    print(1)
    with sqlite3.connect("WebContent Downloader/Local databases/videos.sqlite") as vdb:
        cur = vdb.cursor()
        cur.execute(f"""
                INSERT INTO App_settings(title, thumbnail) VALUES("{title}", "{thumbanail}")
                """)


def updateSettings(settings: tuple):
    dir = settings[0]
    tray = settings[1]
    ffmpeg_dir = settings[2]
    print(dir, tray)
    with sqlite3.connect("app_settings.sqlite") as db:
        cur = db.cursor()
        cur.execute(f"""
        UPDATE App_settings
        SET Directory_to_save = "{dir}",
            Hide_in_tray = "{tray}",
            Ffmpeg_path = "{ffmpeg_dir}";
        """)
