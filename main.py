from data_collection.genre_analise import *
from data_collection.data_base import *

print("Введите название книги из каталога")
name = input()
dict_of_words = get_dict_dif(name)
difficult = difficult1(dict_of_words)

# Rouling_Harry_Potter_1_Harry_Potter_and_the_Sorcerers_Stone_RuLit_Net.txt   23
# Doyle Arthur. A Study in Scarlet - royallib.ru.txt   28
# Li_To-Kill-a-Mockingbird_2_Go-Set-a-Watchman_RuLit_Me.txt 25

print("Сложность книги в процентах: " + str(difficult) + "%")
