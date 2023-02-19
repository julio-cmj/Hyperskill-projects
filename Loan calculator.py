import math
import argparse as arg

def nominal_interest_rate(loan_interest):
    i = loan_interest / (12*100) 
    return i
    
def ordinary_annuity(P,n,i):
    term = (1 + i) ** n
    A = P * ((i*term) / (term - 1)) 
    return A

def loan_principal(A,n,i):
    term = (1 + i) ** n
    P = A / ((i*term) / (term - 1))
    return P

def number_of_payments(A,P,i):
    n = math.log(A / (A - (i*P)), 1 + i)
    return n

def overpayment(P,A,n):
    return A*n - P

def differentiated_payment(P,n,i,m):
    D = (P / n) + i * (P - (P * (m - 1) / n))
    return D


parser = arg.ArgumentParser()
parser.add_argument('--type', choices = ['annuity', 'diff'])
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')
args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]

type = str(arguments[0])


try:
    if type == 'annuity':
        if arguments[1] == None:
            A = float(arguments[4])
            n = float(arguments[2])
            loan_interest = float(arguments[3])
    
            i = nominal_interest_rate(loan_interest)
            P = loan_principal(A, n, i)
    
            print(f"Your loan principal = {P}!")
            print('overpayment = ', overpayment(P, A, n))
            
        if arguments[2] == None:
            P = float(arguments[1])
            A = float(arguments[4])
            loan_interest = float(arguments[3])
        
            i = nominal_interest_rate(loan_interest)
            n = math.ceil(number_of_payments(A,P,i))
    
            time = ''
            years = math.floor(n / 12)
            months = n % 12
    
            if years > 0:
                time += str(years) + ' year'
                if years > 1:
                    time += 's'
            if years >= 1 and months > 0:
                    time += ' and '
            if months > 0:
                time += str(months) + ' month'
                if months > 1:
                    time += 's'
            
            print(f"It will take {time} to repay this loan!")
            print('overpayment = ', overpayment(P, A, n))
    
        if arguments[4] == None:
            P = float(arguments[1])
            n = float(arguments[2])
            loan_interest = float(arguments[3])
        
            i = nominal_interest_rate(loan_interest)
            A = math.ceil(ordinary_annuity(P, n, i))
    
            print(f"Your monthly payment = {A}!")
            print('overpayment = ', overpayment(P, A, n))
    
  
    
    if type == 'diff':
        P = float(arguments[1])
        n = float(arguments[2])
        loan_interest = float(arguments[3])
        i = nominal_interest_rate(loan_interest)
        
        m = 1
        total = 0 
        while m <= n:
            D = math.ceil(differentiated_payment(P,n,i,m))
            print(f"Month {m}: payment is {D}")
            m += 1
            total = total + D
            if m > 50:
                break
        print ('overpayment = ', P - total)
        
except Exception:
    print("Incorrect parameters.")