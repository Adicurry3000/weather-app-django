import pandas as pandas
import requests
from bs4 import BeautifulSoup


page = requests.get('https://weather.com/en-IN/weather/tenday/l/eb99e166853daedcdaaf48d354517f7d64890821240929f01cd3afb6a4014ce8')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='region region-main')
items = week.find_all(class_='twc-table-shadow sticky')
item = week.find_all(class_='day-detail clearfix')
it = [its.find(class_='day-detail clearfix').get_text() for its in item]
print(it)
