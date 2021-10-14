import string


def rewrite(str1, str2):
    f = open(str1, "r")
    g = open(str2, "w")
    while True:
        s = f.readline()
        if not s:
            break
        eng = s.split('\t')[0]
        rus = s.split('"')[-2]

        g.write(eng + "\t" + rus.lower() + "\n")
    f.close()
    g.close()


def more_rewrite(str1, str2):
    f = open(str1, "r")
    g = open(str2, "a")
    words = count_words(str2)
    while True:
        s0 = f.readline()
        s1 = (f.readline().split('\t'))[0]
        if not s0:
            break
        s0 = s0.replace('\n', '')
        s1 = s1.replace('\n', '')
        if len(s0.split(' ')) == 1 and len(s1) <= 59 and s0 not in words:
            g.write(s0 + '\t' + s1 + '\n')
    f.close()
    g.close()


def max_len(str1):
    f = open(str1, 'r')
    m = 0
    while 1:
        s = f.readline()
        m = max(m, len(s))
        if not s:
            break
    print(m)


def len_distribution(str1, maxx):
    f = open(str1, 'r')
    m = {i: 0 for i in range(maxx + 1)}
    i = 0
    while 1:
        s = f.readline()
        m[len(s)] += 1 if i % 2 == 0 else 1
        if not s:
            break
        i += 1
    f.close()
    return m


def count_symbols(text):
    f = open(text, 'r')
    a = dict()
    while 1:
        st = f.readline()
        if not st:
            break
        for i in st:
            if i in a:
                a[i] += 1
            else:
                a[i] = 0
    f.close()
    return a


def count_words(text):
    f = open(text, 'r')
    a = dict()
    while 1:
        st = f.readline()
        if not st:
            break
        temp = st.split('\t')[0]
        if temp in a:
            a[temp] += 1
        else:
            a[temp] = 1
    f.close()
    return set(a.keys())


rewrite(r"dictionaries\best_dict1.txt", "final.txt")
more_rewrite(r"dictionaries\enrus1.txt", 'final.txt')
# for i in count_symbols(r"dictionaries\best_dict1.txt").items():
#   print(i)

print(len(count_words('final.txt')))
