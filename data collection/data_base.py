import pymysql as pms

db_dict = pms.connect(
    host="localhost",
    user="root",
    passwd=""
)

cur = db_dict.cursor()
cur.execute("CREATE DATABASE dictdb;")

query = "CREATE TABLE Dictionary(en_word CHAR(255) , ru_word CHAR(255));"

f = open("enrus1.txt", 'r')

while 1:
    s0 = f.readline()
    s1 = f.readline()
    query1 = f"INSERT INTO Dictionary(en_word, ru_word) VALUES('{s0}, '{s1}');"
    if not s0:
        break
    cur.execute(query1)

f.close()
cur.close()
