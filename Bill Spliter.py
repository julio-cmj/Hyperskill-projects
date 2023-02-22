import random

guests_num = int(input("Enter the number of friends joining (including you):\n"))

while True:
    if guests_num > 0:
        print("Enter the name of every friend (including you), each on a new line:")
        guests_names = [input() for _ in range(0,guests_num)]
    else: 
        print('No one is joining for the party')
        break
        
    bill = int(input('Enter the total bill value:\n'))

    lucky_one = input('Do you want to use the "Who is lucky?" feature? Write Yes/No\n')
    if lucky_one == 'Yes':
        lucky = random.choice(guests_names)
        print (f'{lucky} is the lucky one!')
        bill = round(bill / (len(guests_names) - 1), 2)
        guests = dict.fromkeys(guests_names, bill)
        guests[lucky] = 0
        
    else:
        print('No one is going to be lucky')
        bill = round(bill / len(guests_names), 2)
        guests = dict.fromkeys(guests_names, bill)
    
    print(guests)
    break