from data_collection.genre_analise import *
from data_collection.data_base import *

print("Введите название книги из каталога")
name = input()
dict_of_words = get_dict_dif(name)
# Fifty_Inventions_That_Shaped_th_-_Tim_Harford_1.txt
difficult = difficult1(dict_of_words)
print("Сложность книги в процентах: " + str(round(difficult, 1)) + "%")
