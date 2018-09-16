import sqlite3
import pandas as pd

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

def insertTranslation(c, row):
	c.execute("""update tafsir_sagheer set footnotes_text = :text 
	where chapter_id = :chapter_id and verse_id = :verse_id""",
	{'chapter_id': row['chapter_id'], 'verse_id': row['verse_id'], 'text': row['text']})

def convertNullToEmpty(c):
	c.execute('''update tafsir_sagheer set footnotes_text = "" where footnotes_text is null''')

xl = pd.ExcelFile("TafseerSageerFootnotes.xlsx")
translation = xl.parse('TafseerSageerFootnotes')

conn, c = connectDb("quran_db.sqlite")

# createTable(c)

for index, row in translation.iterrows():
	insertTranslation(c, row)

convertNullToEmpty(c)

closeDb(conn, c)