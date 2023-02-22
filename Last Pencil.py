import random


def valid_pencil():
    number = input()
    try:
        number = int(number)
        if number <= 0:
            print("The number of pencils should be positive")
            number = valid_pencil()
    except Exception:
        print("The number of pencils should be numeric")
        number = valid_pencil()
    return int(number)


def bot_play(pencils):
    if pencils in [5 + n*4 for n in range(0, 40)]:
        return random.randint(1, 3)
    elif pencils in [4 + n*4 for n in range(0, 40)]:
        return 3
    elif pencils in [3 + n*4 for n in range(0, 40)]:
        return 2
    elif pencils in [2 + n*4 for n in range(0, 40)]:
        return 1
    else:
        return 1


def player_play():
    play = input()
    if play not in ['1', '2', '3']:
        print("Possible values: '1', '2' or '3'")
        play = player_play()
    return int(play)


print("How many pencils would you like to use:")
pencils = valid_pencil()

while True:
    player = input("Who will be the first (John, Jack):")
    if player != "John" and player != "Jack":
        print("Choose between 'John' and 'Jack'")
        continue
    break

print("|" * pencils)
print(f"{player}'s turn:")

while pencils != 0:
    if player == 'John':
        play = player_play()
        if pencils - play < 0:
            print("Too many pencils were taken")
            continue
        player = 'Jack'
        if pencils - play == 0:
            print(f"{player} won!")
            break

    elif player == 'Jack':
        play = bot_play(pencils)
        print(play)
        if pencils - play < 0:
            print("Too many pencils were taken")
            continue
        player = 'John'
        if pencils - play == 0:
            print(f"{player} won!")
            break

    pencils -= play
    print("|" * pencils)

    print(f"{player}'s turn:")
