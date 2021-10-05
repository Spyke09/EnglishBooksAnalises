import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def search_url(name, sort="date"):
    return "https://www.rulit.me/books/en/1/" + sort + "?search=" + name


def page_generator(url, max_val):
    val = 0
    index = url.find('1')
    st = url[:index]
    fn = url[index + 1:]
    while max_val > val:
        val += 1
        yield st + str(val) + fn


def search_int(str1):
    st = 0
    temp = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    while str1[st] not in temp:
        st += 1
    fn = st
    while str1[fn] in temp:
        fn += 1
    return st, fn


def next_page(url, max_val):
    st, fn = search_int(url)
    return url[:st] + str(min(int(url[st:fn]) + 1, max_val)) + url[fn:]


def get_last_page(url):
    try:
        r = requests.get(url)
        r = bs(r.text, 'html.parser')
        temp = (r.find_all(class_="pagination pull-right"))
        for i in temp:
            for j in i.find_all('li'):
                t = j.find(title="Последняя страница")
                if t:
                    temp = t['href']

        si = search_int(temp)
        return int(temp[si[0]:si[1]])
    finally:
        return 1


main_url = "https://www.rulit.me/books/en/1/popular"

temp1 = search_url("selgkjewgkljew")

print(get_last_page(temp1))
