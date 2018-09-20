import regex as re
import sqlite3
table_name = "pir_salahuddin"

def connectDb(name):
    conn = sqlite3.connect(name)
    return conn, conn.cursor()

def closeDb(conn, c):
    conn.commit()
    c.close()

def createTable(c):
    c.execute("DROP TABLE IF EXISTS " + table_name)
    c.execute("CREATE TABLE " + table_name + " (id integer primary key, chapter_id INTEGER, verse_id INTEGER, english_text TEXT)")



def processOutIndividualVerses(full_text):
    lineNum = 0
    while 



    for index, line in enumerate(full_text):
        if line.startswith('[\d]'):
            storeTemp = line
        else:
            storeTemp += line


if line starts with number, store in a variable, if it doesnt, store it with the previous variable. when you get to a point that it starts with a numbr again, put it into database.else:
    

    



    results = re.split(r'^[0-9]', textfile, re.MULTILINE)
    
    #print (results)
    return results
    # for line in results:
    #     verse = ''.join(line)
    #     final = ''.join(verse)
    #     c.execute("INSERT INTO " + table_name + " (english_text) VALUES (:fullString)", {'fullString': final})

def InsertIntoDB(verse):
    sql_statement = "INSERT INTO " + table_name + " (english_text) VALUES ("+ verse +");"
    print (sql_statement)
    #c.execute("INSERT INTO " + table_name + " (english_text) VALUES (:fullString);", {'fullString': verse})

def loopToWriteToDatabase(results):
    for line in results:
        #print (line)
        data = line.split()
        verse = ''.join(data)
        #print (verse)
        InsertIntoDB(data)

def readTextfile():
    file = open('wonderful_quran.txt')
    full_text = file.readlines()
    return full_text

conn, c = connectDb("quran_db.sqlite")
createTable(c)
full_text = readTextfile()
#processOutIndividualVerses(readTextfile)
results = processOutIndividualVerses(full_text)
loopToWriteToDatabase(results)
#insertTranslation(c)
#addChapterVerseNumbers(c)
closeDb(conn, c)
