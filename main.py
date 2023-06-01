import requests
from bs4 import BeautifulSoup
import re

def count_words(text):
    cleaned_text = re.sub('<.*?>', '', text)
    words = cleaned_text.split()
    return len(words)

url = 'https://www.example.com/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
word_count = count_words(text)
print("Кількість слів у тексті сторінки:", word_count)
