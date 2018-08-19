import sqlite3

def deleteTable(c):
	c.execute("DROP TABLE tafsir_sageer_footnotes")

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

conn, c = connectDb("quran_db.sqlite")

deleteTable(c)

closeDb(conn, c)

