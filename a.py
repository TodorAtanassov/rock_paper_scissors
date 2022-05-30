import requests as r
from bs4 import BeautifulSoup
import statistics as st


url = "https://ipinfo.io/"

response = r.get(url)
soup = BeautifulSoup(response.text, features='html.parser')
print(soup)