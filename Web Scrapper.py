import requests
import string
from bs4 import BeautifulSoup
import os


def article_saver(url, article_type):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for article in soup.find_all('article'):
        try:
            if article.find('span', {'class': "c-meta__type"}).get_text() == article_type:
                title = article.find('h3').get_text()
                description = article.find('p').get_text()

                for letter in title:
                    if letter in string.punctuation:
                        title = title.replace(letter, '')
                file_name = '_'.join(title.split())

                with open(file_name + '.txt', 'w') as f:
                    f.write(description)
        except Exception:
            pass


n_pages = int(input())
article_type = input()
base_url = 'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page='

page = 1
while page < n_pages + 1:
    url = base_url + str(page)
    os.mkdir(f'Page_{page}')
    os.chdir(f'Page_{page}')
    article_saver(url, article_type)
    os.chdir('..\\')
    page += 1