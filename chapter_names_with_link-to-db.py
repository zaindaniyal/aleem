import sqlite3
table_name = "chapter_names_with_link"

def connectDb(name):
    conn = sqlite3.connect(name)
    return conn, conn.cursor()

def closeDb(conn, c):
    conn.commit()
    c.close()

def createTable(c):
    c.execute("DROP TABLE IF EXISTS " + table_name)
    c.execute("CREATE TABLE " + table_name + " (id integer primary key, chapter_id INTEGER, verse_id INTEGER, title_text TEXT)")

def insertTranslation(c, file):
    for line in file.readlines():
        data = line.split()
        string = ' '.join (data)
        c.execute("INSERT INTO chapter_names_with_link (title_text) VALUES (:fullString)", {'fullString': string})

def addChapterVerseNumbers(c):
    c.execute("UPDATE " + table_name + " SET chapter_id = (SELECT chapter_id FROM verses WHERE id = " + table_name + ".id);")
    c.execute("UPDATE " + table_name + " SET verse_id = (SELECT verse_id FROM verses WHERE id = " + table_name + ".id);")

def readTextfile(c):
    file = open('chapter_names_with_link.txt')
    return file

conn, c = connectDb("quran_db.sqlite")
createTable(c)
readTextfile = readTextfile(c)
insertTranslation(c, readTextfile)
addChapterVerseNumbers(c)
closeDb(conn, c)