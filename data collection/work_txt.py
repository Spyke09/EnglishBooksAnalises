import matplotlib.pyplot as plt
import numpy as np


def rewrite(str1, str2, maxx):
    f = open(str1, 'r')
    g = open(str2, "w")
    while True:
        s0 = f.readline()
        s1 = f.readline()
        m = max(len(s0), len(s1))
        if m <= maxx:
            g.write(s0)
            g.write(s1)
        if not s0:
            break
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


l = 255
rewrite("ENRUS.TXT", "enrus1.txt", l)
temp = len_distribution('enrus1.txt', l)
for i in temp.items():
    print(i)

x = np.array(list(temp.keys()))
y = np.log(np.array(list(map(lambda z: z if z > 0 else 1, temp.values()))))

plt.plot(x, y)
plt.show()
