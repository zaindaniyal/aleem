import sqlite3
import os
from pathlib import Path

testfile = Path("final_file.txt")
if testfile.is_file():
    os.remove(testfile)

def connectDb(name):
	conn = sqlite3.connect(name)
	return conn, conn.cursor()

def closeDb(conn, c):
	conn.commit()
	c.close()

conn, c = connectDb("quran_db.sqlite")

c = conn.cursor()
c.execute("select chapter_text from khalifa_rabeh_chapter_introductions")
chapter_introductions = c.fetchall()

c.execute("select chapter_id from khalifah_rabeh_ra")
chapter_id = c.fetchall()

c.execute("select title_text from chapter_names_with_link")
title_text = c.fetchall()

c.execute("select arabic_text from quran_verse_end_symbol")
arabic_text = c.fetchall()

c.execute("select arabic_text from arabic_no_diacritics")
arabic_no_diacritics_text = c.fetchall()

c.execute("select translation_text from tafsir_sagheer")
tafsir_sagheer = c.fetchall()

c.execute("select footnotes_text from tafsir_sagheer")
ts_footnotes = c.fetchall()

c.execute("select translation_text from khalifah_rabeh_ra")
khalifah_rabeh = c.fetchall()

c.execute("select footnotes_text from khalifah_rabeh_ra")
kr_footnotes = c.fetchall()

c.execute("select translation_text, footnotes_text from maulawi_sher_ali")
maulawi_sher_ali = c.fetchall()

c.execute("select english_text from sir_zafrulla_khan_translation")
sir_zafrulla_khan_translation = c.fetchall()

c.execute("select translation_text from pir_salahuddin")
pir_salahuddin_translation = c.fetchall()

c.execute("select footnotes_text from pir_salahuddin")
pir_salahuddin_footnotes = c.fetchall()

file = open('final_file.txt','w')
previous_chapter_id = 0
for i in range (len(title_text)):
    chapter_id_in_string = ' '.join(map(str, chapter_id[i]))
    chapter_id_in_int = int(chapter_id_in_string)
    if previous_chapter_id != chapter_id_in_int:
        file.write(' '.join(chapter_introductions[previous_chapter_id]) + "\n")
        previous_chapter_id = chapter_id_in_int
    file.write(' '.join(title_text[i]) + "\n")
    file.write(' '.join(arabic_text[i]) + "\n")
    file.write(' '.join(arabic_no_diacritics_text[i]) + "\n")
    file.write(" (ت ص):" + ' '.join(tafsir_sagheer[i]) + "\n")
    if ' '.join(ts_footnotes[i]) != "":
        file.write(" (ت ص ح):" + ' '.join(ts_footnotes[i]) + "\n")
    file.write(" (خ ر):" + ' '.join(khalifah_rabeh[i]) + "\n")
    if ' '.join(kr_footnotes[i]) != "":
        file.write(" (خ ر ح):" + ' '.join(kr_footnotes[i]) + "\n")
    file.write("SA: " + str(i + 1) + "." + ' '.join(maulawi_sher_ali[i]) + "\n")
    file.write("SZK: " + ' '.join(sir_zafrulla_khan_translation[i]) + "\n")
    file.write("PS: " + ' '.join(pir_salahuddin_translation[i]) + "\n")
    if ' '.join(pir_salahuddin_footnotes[i]) != "":
        file.write("PS Footnotes: " + ' '.join(pir_salahuddin_footnotes[i]) + "\n")
    file.write("\n")

file.close()
closeDb(conn, c)