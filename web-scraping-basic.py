# import packeges
import requests
from bs4 import BeautifulSoup
# import pandas as pd

# download and parse the HTML
start_url = 'https://en.wikipedia.org/wiki/Tesla,_Inc.'
# download the HTML from start_url
downloaded_html = requests.get(start_url)
# parse HTML with BeautifulSoup and create a soup object
soup = BeautifulSoup(downloaded_html.text, "html.parser")

# save a local copy
with open('downloaded.html', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
# print(soup.prettify())
