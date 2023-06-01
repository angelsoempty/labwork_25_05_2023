import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
def get_external_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    link_tags = soup.find_all('a')
    links = []
    for link in link_tags:
        href = link.get('href')
        if href and not href.startswith('#') and not href.startswith('mailto:'):
            absolute_url = urljoin(base_url, href)
            links.append(absolute_url)
    return links
url = 'https://www.example.com/'
response = requests.get(url)
html = response.text
external_links = get_external_links(html, url)

if external_links:
    print("Зовнішні посилання на інші сторінки:")
    for link in external_links:
        print(link)
else:
    print("Зовнішні посилання на інші сторінки не знайдено")
