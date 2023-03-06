import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore


def url_checker():
    while True:
        url = input()
        if url in ['back', 'exit']:
            return url
        try:
            link = requests.get('https://' + url)
            domain = url.split('.')
            domain = domain[0] + '.'
            return link, domain
        except Exception:
            print('Invalid URL')


def folder_checker(folder):
    try:
        os.mkdir(folder)
        os.chdir(folder)
    except Exception:
        os.chdir(folder)


def file_checker(file):
    try:
        os.access(file)
        with open(file, 'r', encoding='utf-8') as r:
            r.read()
    except Exception:
        raise FileNotFoundError


def url_display(url, domain):
    soup = BeautifulSoup(url.content, 'html.parser')

    list = []
    for i in soup.find_all('a'):
        if i.get('href') != None:
            list.append(Fore.BLUE + i.get_text())
            pass

    list = [s for s in '\n'.join(list).splitlines() if s]
    formatted_text = '\n'.join(list) + soup.get_text()

    print(formatted_text)
    with open(domain, 'w', encoding='utf-8') as f:                   # create a file
        f.write(formatted_text)


def back():
    print(stack[0])
    stack.popleft()


command_line = sys.argv
dir = command_line[1]

folder_checker(dir)  # checks if the folder already exists
stack = deque()      # create stack

while True:
    url = url_checker()
    if url == 'exit':
        break

    elif url == 'back':
        if len(stack) == 0:
            continue
        else:
            back()

    else:
        try:
            file_checker(url[1])
        except FileNotFoundError:
            url_display(url[0], url[1])

    stack.append(url)