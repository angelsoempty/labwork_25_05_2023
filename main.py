import requests
from bs4 import BeautifulSoup
def get_page_images(html):
    soup = BeautifulSoup(html, 'html.parser')
    image_tags = soup.find_all('img')
    images = []
    for img in image_tags:
        src = img.get('src')
        images.append(src)
    return images

url = 'https://www.example.com/'
response = requests.get(url)
html = response.text
images = get_page_images(html)

if images:
    print("Зображення на сторінці:")
    for image in images:
        print(image)
else:
    print("Зображення на сторінці не знайдено")
