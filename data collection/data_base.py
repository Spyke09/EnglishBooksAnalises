import sqlite3 as sq
import os


def create_bd():
    if os.path.exists("dict.db"):
        os.remove("dict.db")
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Dictionary(
        en_word CHAR(71) , 
        ru_word CHAR(71));
    """)
    conn.commit()

    f = open("final.txt", 'r')

    while 1:
        s = f.readline()
        if not s:
            break
        temp = s.replace('\n', '')
        temp = temp.split('\t')
        if (len(temp)>2):
            print('aboba')
        if (len(temp)<2):
            print('abiba')
        cur.execute(f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{temp[0]}', '{temp[1]}');")

    conn.commit()
    f.close()
    cur.close()
    conn.close()


def translate(st):
    if not os.path.exists("dict.db"):
        create_bd()
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Dictionary WHERE en_word LIKE '{st}';")

    temp = cur.fetchall()
    res = [[i[0]]+i[1].split('\t') for i in temp]

    cur.close()
    conn.close()
    return res


for i in translate('aboba'):
    print(i)
