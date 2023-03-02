import json
import requests

selected_currency = input('Enter your currency code: ')

currency_rates_json = requests.get(f'http://www.floatrates.com/daily/{selected_currency}.json')
currency_rates_dict = dict(json.loads(currency_rates_json.text))

while True:
    selected_rate = input('Enter the currency code you want to convert for: ')
    if selected_rate == '':
        break
    money = float(input('Enter the value: '))
    
    rate = currency_rates_dict[selected_rate]['rate']

    print(f'This amount worths {round(money * rate, 2)} {selected_rate.upper()}')