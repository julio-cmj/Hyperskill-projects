import random

def hangman_game():
    words = ['python', 'java', 'swift', 'javascript']
    english_letters = 'a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
    english_letters = english_letters.split(', ')

    to_guess = random.choice(words)
    response = to_guess
    output = ['-' for n in range(0,len(to_guess))]
    to_guess = '-'.join(to_guess)
    attemp = 0 
    control = 0
    guessed = []
    
    while True:
        
        print(''.join(output))
        guess = input("Input a letter:")
    
        if len(guess) != 1:
            print('Please, input a single letter')
            continue
        elif guess not in english_letters:
            print('Please, enter a lowercase letter from the English alphabet.')
            continue
            
        if guess in guessed:
            print("You've already guessed this letter.")
        elif guess in set(to_guess):
            list = to_guess.split('-')
            for n in range(0,to_guess.count(guess)):
                index = list.index(guess)
                output[index] = guess
                list[index] = ''
        else:
            print("That letter doesn't appear in the word.")
            attemp += 1
        guessed.append(guess)
        
        if attemp > 7:
            print('You lost!')
            return False
        if response == ''.join(output):
            print(f'You guessed the word {response}!')
            print('You survived!')
            return True
            
        if control > 20:
            break
        control += 1

print('''H A N G M A N''')
victories = 0
losses = 0

while True:
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')

    if menu == 'play':
        game = hangman_game()
        if game:
            victories += 1
        else:
            losses += 1
    elif menu == 'results':
        print(f'''You won: {victories} times.
You lost: {losses} times.''')
    elif menu == 'exit':
        break