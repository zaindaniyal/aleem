import argparse
import re
import sqlite3


parser = argparse.ArgumentParser(description='')
parser.add_argument('src_txt', help="The input text file path")
parser.add_argument('db_name', help="The output sqlite file path")
args = parser.parse_args()


def create_translation(line):
	parts = line.split("حاشیہ")
	translation = parts[0].strip()
	footnotes = parts[1:]
	chapter = ""
	verse = ""
	return {"c": chapter, "v": verse, "t": translation, "f": footnotes}


def readTextSource(file_name):
	translation = []
	with open(file_name, 'r') as text_file:
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
	c.execute("DROP TABLE IF EXISTS khalifah_rabeh_ra")
	c.execute("CREATE TABLE khalifah_rabeh_ra (id integer primary key, chapter_id INTEGER, verse_id INTEGER, translation_text TEXT, footnotes_text TEXT)")

def insertTranslation(c, translation):
	c.execute("INSERT INTO khalifah_rabeh_ra (chapter_id, verse_id, translation_text, footnotes_text) VALUES(?, ?, ?, ?)", (translation['c'], translation['v'], translation['t'], ""))

translation = readTextSource(args.src_txt)

conn, c = connectDb(args.db_name)

createTable(c)

for item in translation:
	insertTranslation(c, item)

closeDb(conn, c)
