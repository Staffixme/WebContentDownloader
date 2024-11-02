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


def updateSettings(settings: tuple):
    dir = settings[0]
    tray = settings[1]
    print(dir, tray)
    with sqlite3.connect("app_settings.sqlite") as db:
        cur = db.cursor()
        cur.execute(f"""
        UPDATE App_settings
        SET Directory_to_save = "{dir}",
            Hide_in_tray = "{tray}";
        """)
