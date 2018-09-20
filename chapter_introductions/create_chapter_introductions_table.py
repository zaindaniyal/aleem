import sqlite3

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

def createTable(c):
	c.execute("DROP TABLE IF EXISTS khalifa_rabeh_chapter_introductions")
	c.execute("CREATE TABLE khalifa_rabeh_chapter_introductions (id integer primary key, chapter_id INTEGER, chapter_text TEXT)")

def insertChapterIntroductions(c, chapter, text):
	c.execute("INSERT INTO khalifa_rabeh_chapter_introductions (chapter_id, chapter_text) VALUES(:chapter_id, :chapter_text)",
	{'chapter_id': chapter, 'chapter_text': text})

conn, c = connectDb("quran_db.sqlite")

createTable(c)

for i in range(114):
    chapter = i + 1
    path = f"{chapter}.txt"
    chapter_introduction = open(path)
    text = chapter_introduction.read()
    insertChapterIntroductions(c, chapter, text)

closeDb(conn, c)