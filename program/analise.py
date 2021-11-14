import json
import nltk
from itertools import chain
from program import translator as tr
from nltk.corpus import stopwords
from src.utils import get_root


# функция-генератор получает на входе путь к файлу txt и выдает слова
def word_file_gen(st: str):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
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
    stop_words = set(stopwords.words('english'))
    words = set()
    for i in word_file_gen(st):
        if tl.translate(i) and not (i in words):
            words.add(i)

    count_simple = 0
    filename = get_root('data_collection/set_of_words/most common.txt')
    for i in simple_file_gen(filename):
        if i in words and i not in stop_words:
            count_simple += 1
    return round(count_simple / len(words) * 100)


# функция выдающая словарь с распределением слов и сохраняющая словарь в json файл
def words_distribution(st, _sorted=True):
    dry = dict()
    stopWords = set(stopwords.words('english'))
    for i in word_file_gen(st):
        if i not in stopWords:
            if i in dry:
                dry[i] += 1
            else:
                dry[i] = 1

    _delete_s(dry)
    sort_dry = sort_dict(dry)

    with open(get_root('program/dict_words.json'), 'w') as js:
        json.dump(sort_dry if _sorted else dry, js)


# убирает окончания в англ. словах
def _delete_s(dry: dict):
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
def print_word_d():
    with open(get_root('program/dict_words.json'), 'r') as js:
        d = json.load(js)
        for i, j in d.items():
            print(f"{i}: {j}")


# выдает часть словаря
def get_piece_dict(d: dict, border=20):
    border = min(max(d.values()) / 2, border)
    dic = dict()
    for i, j in d.items():
        dic[i] = j
        if j < border:
            break
    return dic


# функция, выдающаяя жанровое распределение книги
def genre_distribution(border):
    with open(get_root('program/dict_words.json'), 'r') as js:
        d = json.load(js)
    names = set(simple_file_gen(get_root(r'data_collection\set_of_words\names.txt')))
    with open(get_root('data_collection/genres.json'), 'r') as js:
        genre = json.load(js)
        genre['fiction'] = names

    dic = get_piece_dict(d, border)

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
    so = sorted(d, key=d.get, reverse=True)
    for i in so:
        res[i] = d[i]
    return res


def _clear_ease_words(d: dict):
    stopWords = set(stopwords.words('english'))
    names = set(simple_file_gen(get_root(r'data_collection\set_of_words\names.txt')))
    filename = get_root('data_collection/set_of_words/most common.txt')
    for i in chain(simple_file_gen(filename), stopWords, names):
        if i in d:
            d.pop(i)


def get_difficult_data(n: int, translate_n, _ease=True):
    with open(get_root('program/dict_words.json'), 'r') as js:
        d: dict = json.load(js)

    if not _ease:
        _clear_ease_words(d)

    tra = tr.Translator()
    sum_v = sum(d.values())
    i = 0

    for j, k in d.items():
        if i == n:
            break
        t = tra.translate(j)
        if not t:
            continue
        i += 1
        yield k / sum_v, j, t[:translate_n]
