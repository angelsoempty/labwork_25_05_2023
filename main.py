import requests
from bs4 import BeautifulSoup
def get_page_title(html):
    soup = BeautifulSoup(html, 'html.parser')
    title_tag = soup.title
    if title_tag:
        return title_tag.string.strip()
    else:
        return None
url = 'https://www.example.com/'
response = requests.get(url)
html = response.text
title = get_page_title(html)
if title:
    print("Заголовок сторінки:", title)
else:
    print("Заголовок сторінки не знайдено")
