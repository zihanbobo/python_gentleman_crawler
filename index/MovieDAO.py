import sqlite3
import time

def getConnect():
    return sqlite3.connect('D://Workspace//pythonWorkspace//python_gentleman_crawler//db//database.db')

def saveMovie(av):
    conn = getConnect()

    avNumber = av["av_number"]
    remoteCover = av["remote_cover"]
    actor = av["actor"];
    publicTime = av.get("public_time", None)
    title = av.get("title")

    cursor = conn.cursor()
    cursor = cursor.execute("SELECT * from t_movies where av_number=?", [avNumber])

    if (len(cursor.fetchall()) > 0):
        return True

    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    cursor.execute("insert into t_movies (av_number, actor, title, remote_cover, create_time, public_time) values (?, ?, ?, ?, ?, ?)",
                   [avNumber, actor, title, remoteCover, now, publicTime])
    conn.commit()
    conn.close()

    return False


def updateMovieFile(av):
    conn = getConnect()
    cursor = conn.cursor()

    avNumber = av["av_number"]
    local_movie = av.get("local_movie")
    cursor.execute("update t_movies set local_movie=? where av_number=?",
        [local_movie, avNumber])

    conn.commit()
    conn.close()