import sqlite3

def getHtmlCachePath(name):
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/temp/" + name

def getConnect():
    return sqlite3.connect('/var/services/homes/lijl/dev/python_gentleman_crawler/db/database.db')

def getSimiConnect():
    return sqlite3.connect('/var/services/homes/lijl/dev/python_gentleman_crawler/db/db-similar.db')

def getRootPath():
    return "/var/services/homes/lijl/drivers/etc/kodl"

def getVRPath():
    return "/var/services/homes/lijl/drivers/etc/kodl/ring"

def getClassicPath():
    return "/var/services/homes/lijl/drivers/etc/kodl/classic"

def getTextPath():
    return "/var/services/homes/lijl/drivers/etc/kodl/trash"
   
def getImageCachePath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/images/"

def getImageTempPath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/static/temp/"

def getVRTrainDataPath():
    return "/var/services/homes/lijl/dev/python_gentleman_crawler/data/vr/"