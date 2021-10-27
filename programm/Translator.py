import sqlite3 as sq


class Translator:
    def __init__(self):
        self._conn = conn = sq.connect('data_collection\dict_without_repeates.db')
        self._cur = conn.cursor()

    def translate(self, word: str):
        self._cur.execute(f"SELECT ru_word FROM Dictionary WHERE en_word = '{word}';")
        temp = self._cur.fetchall()
        temp = temp[0][0].split('\t')
        return temp
