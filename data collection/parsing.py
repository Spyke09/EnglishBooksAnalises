import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

main_url = "https://www.rulit.me/"
r = requests.get(main_url)
soup = bs(r.text, "html.parser")
temp = [i.a['href'] + '/en/1/rating' for i in (soup.find('ul', class_='dropdown-menu')).find_all('li')]

for i in temp:
    print(i)
