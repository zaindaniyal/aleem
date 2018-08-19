import sqlite3
import pandas as pd

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

def createTable(c):
	c.execute("DROP TABLE IF EXISTS tafsir_sageer_footnotes")
	c.execute("CREATE TABLE tafsir_sageer_footnotes (id integer primary key, chapter_id INTEGER, verse_id INTEGER, footnotes_text TEXT)")

def insertTranslation(c, row):
	c.execute("""UPDATE tafsir_sagheer SET footnotes_text = :text 
	WHERE chapter_id = :chapter_id AND verse_id = :verse_id""",
	{'chapter_id': row['chapter_id'], 'verse_id': row['verse_id'], 'text': row['text']})

xl = pd.ExcelFile("TafseerSageerFootnotes.xlsx")
translation = xl.parse('TafseerSageerFootnotes')

conn, c = connectDb("quran_db.sqlite")

# createTable(c)

for index, row in translation.iterrows():
	insertTranslation(c, row)

closeDb(conn, c)