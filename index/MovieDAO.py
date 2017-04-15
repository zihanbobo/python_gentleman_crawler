import sqlite3
import time

def saveAvNumberPic(av):
    conn = sqlite3.connect('../db/database.db')

    avNumber = av["av_number"]
    remoteCover = av["remote_cover"]
    actor = av["actor"];

    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_movies where av_number=?", [avNumber])

    if (len(cursor.fetchall()) > 0):
        return

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    cursor.execute("insert into t_movies (av_number, actor, remote_cover, create_time) values (?, ?, ?, ?)",
                   [avNumber, actor, remoteCover, now])
    conn.commit()

    conn.close()