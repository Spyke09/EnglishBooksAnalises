import data_base


def words_gen():
    f = open(r'set of words\3000.txt', 'r')
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


easy_words()

