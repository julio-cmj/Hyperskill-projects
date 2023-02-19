msgs = ["Enter an equation", 
        "Do you even know what numbers are? Stay focused!", 
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        'Yeah... division by zero. Smart move...',
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

memory = 0

def is_one_digit(v):
    return v > -10 and v < 10 and v.is_integer()

while True:
    msg = ''
    mensagem = input(msgs[0])
    x, oper, y = mensagem.split()

    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    
    try:
        x = float(x)
        y = float(y)
    except Exception:
        print(msgs[1])
        continue
    if oper == '+' or oper == '-' or oper == '/' or oper == '*':
        pass
    else:
        print(msgs[2])
        continue
    
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msgs[6]
    if x == 1.0 or y == 1.0 and oper == '*':
        msg = msg + msgs[7]
    if (x == 0 or y == 0) and (oper == '+' or oper == '-' or oper == '*'):
        msg = msg + msgs[8]
    if msg != '':
        msg =  msgs[9] + msg 
        print(msg)
    
    if oper == '+':
        result = x + y
    elif oper == '-':
        result = x - y
    elif oper == '*':
        result = x * y
    elif oper == '/' and y != 0:
        result = x / y
    else:
        print(msgs[3])
        continue
    print(result)

    answer = input(msgs[4])
    if answer == 'y' and is_one_digit(result):
        msg_index = 10
        while True: 
            answer = input(msgs[msg_index])
            if answer == 'n':
                break
            elif msg_index == 12:
                memory = result
                break
            else:
                msg_index += 1
            
    elif answer == 'y' and not is_one_digit(result): 
            memory = result
    

    answer = input(msgs[5])
    if answer == 'y':
        continue
    break