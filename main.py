import json

from programm import translator as tr
from programm import analise as an

a = tr.Translator()
book1 = r'C:\Users\ad.romanov\Downloads\books\The Holy Bible.txt'

an.print_word_d(book1)

print(an.genre_distribution(book1))



