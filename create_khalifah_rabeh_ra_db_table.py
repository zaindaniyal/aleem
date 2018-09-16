import sqlite3
table_name = "khalifah_rabeh_ra"

def create_translation(line):
	parts = line.split("حاشیہ")
	translation = parts[0].strip()
	footnotes = ""
	if (len(parts) == 2):
		footnotes = parts[1].strip().strip(":").strip()
	chapter = ""
	verse = ""
	return {"c": chapter, "v": verse, "t": translation, "f": footnotes}


def readTextSource(file_name):
	translation = []
	with open(file_name) as text_file:
		for line in text_file:
			translation.append(create_translation(line))
	return translation

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

def createTable(c):
	c.execute("DROP TABLE IF EXISTS "+ table_name)
	c.execute("CREATE TABLE " + table_name + "(id integer primary key, chapter_id INTEGER, verse_id INTEGER, translation_text TEXT, footnotes_text TEXT)")

def insertTranslation(c, translation):
	c.execute("INSERT INTO " + table_name + "(chapter_id, verse_id, translation_text, footnotes_text) VALUES(?, ?, ?, ?)", (translation['c'], translation['v'], translation['t'], translation['f']))

def addChapterVerseNumbers(c):
    c.execute("UPDATE " + table_name + " SET chapter_id = (SELECT chapter_id FROM verses WHERE id = " + table_name + ".id);")
    c.execute("UPDATE " + table_name + " SET verse_id = (SELECT verse_id FROM verses WHERE id = " + table_name + ".id);")

translation = readTextSource("KhalifaRabehTarjamaWFootnotes.txt")

conn, c = connectDb("quran_db.sqlite")

createTable(c)

for item in translation:
	insertTranslation(c, item)
addChapterVerseNumbers(c)

closeDb(conn, c)
