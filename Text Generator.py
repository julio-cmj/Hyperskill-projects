# text generator based on simple markov chains and b-gram language model, with some personal modifications

from nltk import tokenize
from nltk.corpus import gutenberg
import random
import re


def corpus_statistics():
    """Display Corpus Statistics"""
    print('Corpus statistics')
    print(f'All tokens: {len(file_tokenized)}')
    print(f'Unique tokens: {len(set(file_tokenized))}')
    print(f'Number of bigrams: {len(bigrams)}')


def start_word(word_list: 'list where the word should be picked') -> 'returns a word if "start word" conditions':
    """Pick a random word wich: always start with capitalized and
     not ends with a sentence-ending punctuation mark"""
    while True:
        word = random.choice(word_list)
        if bool(re.match('^[A-Z].+[^\W],?$', word)) is True:
            return word
        else:
            continue


def phrase_maker():
    """Prints a phrase with at least 5 words"""
    word = start_word(file_tokenized)
    phrase = [word]
    while len(phrase) < 5 or bool(re.match('.*[!?\.]', word)) is not True:
        probability = 0
        for key, value in bigrs.get(word).items():
            if len(bigrs.get(word)) == 1:  # prevents the same word from get repeated in sequence
                word = key
            if value > probability and random.randint(0, 1) == 1:
                probability = value
                word = key
        phrase.append(word)

    print(' '.join(phrase))


def bigram_spliter(tokens: 'list of tokens') -> 'list of bigrams':
    """Create bigrams given a list of tokens"""
    bigrams = []
    for n in range(len(tokens)):
        try:
            head = tokens[n]
            tail = tokens[n + 1]
            bigrams.append({'Head': head, 'Tail': tail})
        except IndexError:
            pass

    return bigrams


def bigram_normalizer(bigrams: 'list of bigrams') -> 'list of normalized bigrams':
    """Takes a list of bigrams and returns a list with the heads and his tails counts"""
    bigrs = {}
    for bigram in bigrams:
        head = bigram.get('Head')
        tail = bigram.get('Tail')

        if head not in bigrs:
            bigrs.update({head: {}})
            pass

        if tail not in bigrs.get(head):
            bigrs[head].update({tail: 1})
        else:
            bigrs[head][tail] += 1

    return bigrs


# tokenize file text
file_tokenized = []
for file in gutenberg.fileids():
    with gutenberg.open('whitman-leaves.txt') as f:
        tokenized = tokenize.WhitespaceTokenizer().tokenize(f.read())
        file_tokenized.extend(tokenized.copy())

bigrams = bigram_spliter(file_tokenized)
bigrs = bigram_normalizer(bigrams)

# prints the generated text
for _ in range(1):
    phrase_maker()
