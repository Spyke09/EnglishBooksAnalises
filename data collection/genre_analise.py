import data_base
import nltk

genres = ['most common', 'business', 'science', "children's literature", 'fiction', 'art and culture', 'computers',
          'religion', 'history', 'tutorials', ]


def words_gen(st: str):
    f = open(fr'set of words\{st}', 'r')
    while (1):
        a = f.readline()
        a = a.replace("\n", '')
        if not a:
            break
        yield a
    f.close()


def easy_words():
    for i in data_base.translate_gen(words_gen()):
        if i[1] is None:
            print(i)


def read_books():
    f = open(f'set of words\Fifty_Inventions_That_Shaped_th_-_Tim_Harford_1.txt')
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    s = dict()
    while 1:
        try:
            a = f.readline()
        except:
            continue
        if not a:
            break
        a = a.lower()
        for i in tokenizer.tokenize(a):
            if not i in s:
                s[i] = 1.0
            else:
                s[i] += 1.0

    temp = []
    for i in s.keys():
        if not data_base.translate(i):
            temp.append(i)
    for i in temp:
        s.pop(i)
    l = len(s)
    s = sort_dict(s)
    # g = open(r'set of words\res.txt', 'w')
    for i in s.keys():
        s[i] /= l
        print(i, s[i])

    f.close()


def sort_dict(d):
    res = dict()
    so = sorted(d, key=d.get)
    for i in so:
        res[i] = d[i]
    return res


read_books()
