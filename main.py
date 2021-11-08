import json

from programm import translator as tr
from programm import analise as an

a = tr.Translator()
book1 = r'C:\My\Downloads\Grant_The-Shadow_40_The-Death-Triangle_RuLit_Me.txt'

an.print_word_d(book1)

print(an.genre_distribution(book1))



