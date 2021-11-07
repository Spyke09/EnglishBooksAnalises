import nltk
from programm import translator as tr
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


# функция-генератор получает на входе путь к файлу txt и выдает слова
def word_file_gen(st):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    stemmer = SnowballStemmer(language='english')
    names = set(simple_file_gen(r'data_collection\set_of_words\names.txt'))
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
            if i not in names:
                yield i
    f.close()


# фукция-генератор для построчного чтения
def simple_file_gen(st):
    f = open(st, 'r')
    while 1:
        a = f.readline()
        if not a:
            break

        yield a.replace('\n', '')
    f.close()


# анализ текста на сложность - 1й вариант
def difficult_1(st):
    tl = tr.Translator()
    stopWords = set(stopwords.words('english'))
    words = set()
    for i in word_file_gen(st):
        if tl.translate(i) and not (i in words):
            words.add(i)

    count_simple = 0
    for i in simple_file_gen('data_collection\set_of_words\most common.txt'):
        if i in words and not i in stopWords:
            count_simple += 1
    return round(count_simple / len(words) * 100)


# функция выдающее распределение жанров
def genre_distribution(st):
    dry = dict()
    stopWords = set(stopwords.words('english'))
    for i in word_file_gen(st):
        if i not in stopWords:
            if i in dry:
                dry[i] += 1
            else:
                dry[i] = 1
    return dry


# функция сортирующая словарь по второму элементу
def sort_dict(d):
    res = dict()
    so = sorted(d, key=d.get)
    for i in so:
        res[i] = d[i]
    return res
