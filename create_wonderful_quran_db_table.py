# python create_wonderful_quran_db_table.py ../translations/wonderful_quran.txt quran_db.sqlite
import re
import sqlite3

dbName = "quran_db.sqlite"
srcTxt = "wonderful_quran.txt"

def connect_db(name):
    conn = sqlite3.connect(name)
    return conn, conn.cursor()

def close_db(conn, c):
    conn.commit()
    c.close()

def create_table(c, name):
    c.execute("DROP TABLE IF EXISTS " + name)
    c.execute("CREATE TABLE " + name + " (id integer primary key, chapter_id INTEGER, verse_id INTEGER, translation_text TEXT, footnotes_text TEXT);")

def insert_translation(c, tableName, verse):
	c.execute("INSERT INTO " + tableName + " (chapter_id, verse_id, translation_text, footnotes_text) VALUES (:chapterId, :verseId, :translation, :footnotes);", verse)

# match group for verse number and beginning of translation
verseStartPattern = re.compile(r'^(\d+)\.\s(.+)')
# match group for footnote
footnotePattern = re.compile(r'^(\*+.+)')

verses = {}
chapterId = 0
verseId = 0
translation = ""
footnotes = []

def add_verse(chapterId, verseId, translation, footnotes):
	verse = {'chapterId': chapterId, 'verseId': verseId, 'translation': translation.strip(), 'footnotes': '\n'.join(footnotes)}
	if chapterId in verses:
		verses[chapterId][verseId] = verse
	else:
		verses[chapterId] = {verseId: verse}


with open(srcTxt) as file:
	for line in file:
		# Skip empty or blank lines
		if line.strip() == "":
			continue
		
		# Check if start of new verse
		checkVerseStart = re.match(verseStartPattern, line)
		# Check if footnote
		checkFootnote = re.match(footnotePattern, line)
		
		if(checkVerseStart):
			# Clear translation and footnotes
			translation = ""
			footnotes = []
			verseId = checkVerseStart.group(1)
			# Check if new chapter start
			if(verseId == "1"):
				chapterId += 1
				verses[chapterId] = {}
			# Start translation text
			translation = checkVerseStart.group(2).strip()
		
		elif(checkFootnote):
			# Append to footnotes
			footnotes.append(checkFootnote.group(1).strip())
		
		else:
			# Append to translation text
			translation = translation + "\n" + line.strip()

		add_verse(chapterId, verseId, translation, footnotes)


tableName = "pir_salahuddin"
conn, c = connect_db(dbName)
create_table(c, tableName)

for chapterId, chapter in verses.items():
	for verseId, verse in chapter.items():
		insert_translation(c, tableName, verse)

close_db(conn, c)
