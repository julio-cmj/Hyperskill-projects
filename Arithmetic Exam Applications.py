# write your code here
import random


def simple_operations():
    opers = ['+', '-', '*']
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    oper = random.choice(opers)
    print(x, oper, y)

    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y

    return result


def integral_squares():
    x = random.randint(11, 29)
    result = x ** 2
    print(x)

    return result


def check_answer():
    while True:
        answer = input()
        try:
            answer = int(answer)
            return answer
        except Exception:
            print('Wrong format! Try again.')
            continue


def check_mode():
    mode = input("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
    try:
        if int(mode) in [1, 2]:
            return int(mode)
        else:
            raise ValueError
    except Exception():
        print('Wrong format! Try again.')
        check_mode()


mode = check_mode()
mark = 0
count = 0

if mode == 1:
    description = "simple operations with numbers 2-9"
    while count < 5:
        result = simple_operations()
        answer = check_answer()
        if answer == result:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
        count += 1

if mode == 2:
    description = "integral squares with numbers 11-29"
    while count < 5:
        result = integral_squares()
        answer = check_answer()
        if answer == result:
            print('Right!')
            mark += 1
        else:
            print('Wrong!')
        count += 1

save = input(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")

if save in ['yes', 'YES', 'y', 'Yes']:
    name = input("What is your name")
    file = open("results.txt", "a")
    file.write(f"{name}: {mark}/5 in level {mode} ({description}).")
    file.close()
    print('The results are saved in "results.txt".')
else:
    pass
