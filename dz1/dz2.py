import requests
from bs4 import BeautifulSoup
url = 'https://anagram.poncy.ru/words.html?answer_type=3&inword=ростелеком'
r = requests.get(url).text
soup = BeautifulSoup(r, 'html.parser')
print(soup)
