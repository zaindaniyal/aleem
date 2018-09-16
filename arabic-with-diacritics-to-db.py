import sqlite3

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

def createTable(c):
	c.execute("DROP TABLE IF EXISTS arabic_no_diacritics")
	c.execute("CREATE TABLE arabic_no_diacritics (id integer primary key, chapter_id INTEGER, verse_id INTEGER, arabic_text TEXT)")

def insertTranslation(c, file):
	for line in file.readlines():
		data = line.split()
		string = ' '.join (data)
		#print (string)
		c.execute("INSERT INTO arabic_no_diacritics (arabic_text) VALUES (:fullString)", {'fullString': string})

def readTextfile(c):
    file = open('IndoPakArabicNoDiacritics.txt')
    insertTranslation(c, file)

conn, c = connectDb("quran_db.sqlite")

createTable(c)

readTextfile(c)

closeDb(conn, c)