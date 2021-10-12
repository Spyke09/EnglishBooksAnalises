def easy_words():
    f = open(r'set of words\temp.txt', 'r')
    g = open(r'set of words\temp1.txt', 'w')
    l = []
    while (1):
        a = f.readline()
        if not a:
            break
        a = a.replace('\n', '')
        if (a != 'a'):
            g.write(a + '\n')

    f.close()


o = ['sdfs0', 'wdf']
for i in o:
    i = 'sdc'
print(o)