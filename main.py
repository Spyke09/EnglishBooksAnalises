from programm import translator as tr
from programm import analise as an

a = tr.Translator()
book1 = r'data_collection\set_of_words\Li_To-Kill-a-Mockingbird_2_Go-Set-a-Watchman_RuLit_Me.txt'
book2 = r'data_collection\set_of_words\Vens_Elon-Musk_RuLit_Me.txt'
book3 = r'data_collection\set_of_words\Geyts_The_Road_Ahead_RuLit_Net.txt'
book4 = r'data_collection\set_of_words\Phelan_I-m-Sorry-I-broke-Your-Company_RuLit_Net.txt'

for i in an.sort_dict(an.genre_distribution(book4)).items():
    print(i)



