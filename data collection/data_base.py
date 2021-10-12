import sqlite3 as sq
import os


def create_bd():
    if os.path.exists("dict.db"):
        os.remove("dict.db")
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Dictionary(
        en_word CHAR(255) , 
        ru_word CHAR(255));
    """)
    conn.commit()

    f = open("final.txt", 'r')

    while 1:
        s = f.readline()
        if not s:
            break
        temp = s.replace('\n', '')
        temp = temp.split('\t')
        if (len(temp) > 2):
            print('aboba')
        if (len(temp) < 2):
            print('abiba')
        cur.execute(f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{temp[0]}', '{temp[1]}');")

    conn.commit()
    f.close()
    cur.close()
    conn.close()


def indexing():
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute("CREATE INDEX index_name ON Dictionary( en_word );")


def delete_repeates():
    u1 = 0
    u2 = 0
    if os.path.exists("dict2.db"):
        os.remove("dict2.db")
    conn = sq.connect("dict2.db")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE Dictionary(
        en_word CHAR(255) , 
        ru_word CHAR(255));
    """)
    conn.commit()

    conn1 = sq.connect("dict.db")
    cur1 = conn1.cursor()
    cur1.execute(f"SELECT en_word FROM Dictionary;")
    print(len(cur1.fetchall()))
    return 1

    for i in cur1.fetchall():
        cur.execute(f"SELECT * FROM Dictionary WHERE en_word LIKE '{i[0]}';")
        if not cur.fetchone():
            cur1.execute(f"SELECT * FROM Dictionary WHERE en_word LIKE '{i[0]}';")
            temp = cur1.fetchall()
            res = []
            for j in temp:
                res.extend(j[1].split('\t'))
            for j in range(len(res)):
                res[j] = res[j]+'\t'
            res = ''.join(res)
            cur.execute(f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{i[0]}', '{res}');")
            u1 += 1
        else:
            u2 += 1
        if u1 % 100 == 0:
            print(u1, u2)
    conn.commit()
    cur1.close()
    conn1.close()
    cur.close()
    conn.close()


def translate(st: str):
    conn = sq.connect("dict.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM Dictionary WHERE en_word LIKE '{st}';")

    temp = cur.fetchall()
    res = []
    for i in temp:
        res.extend(i[1].split('\t'))

    cur.close()
    conn.close()
    return res


    cur.close()
    conn.close()
    return l

delete_repeates()
