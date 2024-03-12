import pandas as pd
import requests 
from bs4 import BeautifulSoup

url = "https://moviesmod.zip/"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
# box = soup.find("article", class_="latestPost excerpt" )
box = soup.find("h2", class_="title front-view-title" )

print(box)
