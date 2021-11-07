
from data_collection import data_base
import nltk
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer


genres = ['most common', 'business', 'science', "children's literature", 'fiction', 'art and culture', 'computers',
          'religion', 'history', 'tutorials', ]


def words_gen(st: str):
    f = open(fr'data_collection\set of words\{st}', 'r')
    while (1):
        a = f.readline()
        a = a.replace("\n", '')
        if not a:
            break
        yield a
    f.close()


def easy_words():
    for i in data_base.translate_gen(words_gen("most common.txt")):
        if i[1] is None:
            print(i)


def get_dict_dif(st):
    f = open(fr'data_collection\set of words\{st}')
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    snow_stemmer = SnowballStemmer(language='english')
    s = dict()
    length = 0
    stopWords = set(stopwords.words('english'))
    while 1:
        try:
            a = f.readline()
        except:
            continue
        if not a:
            break
        a = tokenizer.tokenize(a.lower())
        for j in a:
            i = snow_stemmer.stem(j)
            if not i in stopWords:
                length += 1
                if not i in s:
                    s[i] = 1.0
                else:
                    s[i] += 1.0

    temp = []
    for i in s.keys():
        if not data_base.translate(i):
            length -= s[i]
            temp.append(i)

    for i in temp:
        s.pop(i)
    s = sort_dict(s)
    # g = open(r'set_of_words\res.txt', 'w')
    for i in s.keys():
        s[i] /= length
    f.close()
    return s


def sort_dict(d):
    res = dict()
    so = sorted(d, key=d.get)
    for i in so:
        res[i] = d[i]
    return res


def difficult1(input_set: dict):
    temp = input_set.copy()
    for i in words_gen("most common.txt"):
        if i in temp:
            temp.pop(i)
    return sum(temp.values()) * 100


def difficult2(input_set: dict):
    l = len(input_set)
    temp = input_set.copy()
    for i in words_gen("most common.txt"):
        if i in temp:
            temp.pop(i)
    return (l - len(temp)) / l


def get_words(input_set: dict):
    temp = input_set.copy()
    l = len(temp)
    for i in words_gen("most common.txt"):
        if i in temp:
            temp.pop(i)
    return temp.keys()


