import json

import nltk
from programm import translator as tr
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from src.utils import get_root



# функция-генератор получает на входе путь к файлу txt и выдает слова
def word_file_gen(st: str):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    stemmer = SnowballStemmer(language='english')
    # names = set(simple_file_gen(get_root(r'data_collection\set_of_words\names.txt')))
    f = open(st, 'r')
    while 1:
        try:
            a = f.readline()
        except:
            continue
        if not a:
            break
        a = tokenizer.tokenize(a.lower())
        for i in a:
            # if i not in names:
            yield i
    f.close()


# фукция-генератор для построчного чтения
def simple_file_gen(st: str):
    f = open(st, 'r')
    while 1:
        a = f.readline()
        if not a:
            break
        yield a.replace('\n', '')
    f.close()


# анализ текста на сложность - 1й вариант
def difficult_1(st: str):
    tl = tr.Translator()
    stopWords = set(stopwords.words('english'))
    words = set()
    for i in word_file_gen(st):
        if tl.translate(i) and not (i in words):
            words.add(i)

    count_simple = 0
    filename = get_root('data_collection/set_of_words/most common.txt')
    for i in simple_file_gen(filename):
        if i in words and not i in stopWords:
            count_simple += 1
    return round(count_simple / len(words) * 100)


# функция выдающая словарь с распределением слов
def words_distribution(st, _sorted=True, _names=True):
    dry = dict()
    names = set(simple_file_gen(get_root(r'data_collection\set_of_words\names.txt')))
    stopWords = set(stopwords.words('english'))
    if _names:
        for i in word_file_gen(st):
            if i not in stopWords:
                if i in dry:
                    dry[i] += 1
                else:
                    dry[i] = 1
    else:
        for i in word_file_gen(st):
            if i not in stopWords and i not in names:
                if i in dry:
                    dry[i] += 1
                else:
                    dry[i] = 1

    delete_s(dry)
    return sort_dict(dry) if _sorted else dry


# убирает окончания в англ. словах
def delete_s(dry: dict):
    tra = tr.Translator()

    for i in dry.keys():
        if len(i) > 3 and i[-1] == 's':
            if i[:-1] in dry and tra.translate(i[:-1]):
                dry[i[:-1]] += dry[i]
                dry[i] = -1
            elif i[:-2] in dry and tra.translate(i[:-2]):
                dry[i[:-2]] += dry[i]
                dry[i] = -1
            elif i[:-3] + 'y' in dry and tra.translate(i[:-3] + 'y'):
                dry[i[:-3] + 'y'] += dry[i]
                dry[i] = -1


# печатает words_distribution
def print_word_d(st, _sorted=True):
    for i, j in words_distribution(st, _sorted).items():
        print(f"{i}: {j}")


# выдает часть словаря
def get_piece_dict(d: dict, t=4):
    dic = dict()
    maxv = max(d.values())
    for i, j in d.items():
        if j >= maxv / t:
            dic[i] = j
    return dic


# функция, выдающаяя жанровое распределение книги
def genre_distribution(st: str):
    d = words_distribution(st)
    names = set(simple_file_gen(get_root(r'data_collection\set_of_words\names.txt')))
    with open(get_root('data_collection/genres.json'), 'r') as js:
        genre = json.load(js)
        genre['fiction'] = names


    dic = get_piece_dict(d,8)

    result = dict()
    for i, j in genre.items():
        count = 0
        for t in j:
            if t in dic:
                count += 1
        result[i] = count

    return result


# функция сортирующая словарь по второму элементу
def sort_dict(d):
    res = dict()
    so = sorted(d, key=d.get)
    for i in so:
        res[i] = d[i]
    return res
