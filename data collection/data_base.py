import sqlite3 as sq
import os
import time


def create_bd():
    if os.path.exists("dict.db"):
        os.remove("dict.db")
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Dictionary(
        en_word TEXT , 
        ru_word TEXT);
    """)

    cur.execute("CREATE INDEX new_ind ON Dictionary(en_word)")
    conn.commit()

    f = open("final.txt", 'r')

    while 1:
        s = f.readline()
        if not s:
            break
        temp = s.replace('\n', '')
        temp = temp.split('\t')
        cur.execute(f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{temp[0]}', '{temp[1]}');")

    conn.commit()
    f.close()
    cur.close()
    conn.close()


def delete_repeates():
    if os.path.exists("dict_without_repeates.db"):
        os.remove("dict2.db")
    conn = sq.connect("dict2.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Dictionary(
        en_word TEXT , 
        ru_word TEXT);
    """)
    conn.commit()

    cur.execute("CREATE INDEX second_ind ON Dictionary (en_word)")

    conn1 = sq.connect("dict.db")
    cur1 = conn1.cursor()
    cur1.execute(f"SELECT en_word FROM Dictionary;")

    for i in cur1.fetchall():
        cur.execute(f"SELECT * FROM Dictionary WHERE en_word = '{i[0]}';")
        if not cur.fetchone():
            cur1.execute(f"SELECT * FROM Dictionary WHERE en_word = '{i[0]}';")
            temp = cur1.fetchall()
            res = []
            for j in temp:
                res.extend(j[1].split('\t'))
            for j in range(len(res)):
                res[j] = res[j] + '\t'
            res = ''.join(res)
            cur.execute(f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{i[0]}', '{res}');")

    conn.commit()
    cur1.close()
    conn1.close()
    cur.close()
    conn.close()


def translate(st: str, base="dict_without_repeates.db"):
    conn = sq.connect(base)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Dictionary WHERE en_word LIKE '{st}';")

    temp = cur.fetchall()
    return temp
    res = []
    for i in temp:
        res.extend(i[1].split('\t'))

    cur.close()
    conn.close()
    return res


def translate_gen(st, base="dict_without_repeates.db"):
    conn = sq.connect(base)
    cur = conn.cursor()
    for i in st:
        cur.execute(f"SELECT * FROM Dictionary WHERE en_word = '{i}';")
        temp = cur.fetchone()
        if temp:
            yield temp
        else:
            yield i, None
    cur.close()
    conn.close()

