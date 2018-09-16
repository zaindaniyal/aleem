import sqlite3
import unicodecsv

def connectDb(name):
    conn = sqlite3.connect(name)
    return conn, conn.cursor()

def closeDb(conn, c):
    conn.commit()
    c.close()

def createTable(c):
    c.execute("DROP TABLE IF EXISTS sir_zafrulla_khan_translation")
    c.execute("CREATE TABLE sir_zafrulla_khan_translation (id integer primary key, chapter_id INTEGER, verse_id INTEGER, english_text TEXT)")

def insertTranslation(c, file):
    for line in file.readlines():
        data = line.split()
        string = ' '.join (data)
        c.execute("INSERT INTO sir_zafrulla_khan_translation (english_text) VALUES (:fullString)", {'fullString': string})

def readTextfile(c):
    file = open('SirZafrullaKhan.txt')

    insertTranslation(c, file)

conn, c = connectDb("quran_db.sqlite")

createTable(c)

readTextfile(c)

closeDb(conn, c)
