import time
from datetime import datetime
income = input('Enter income amount: ')
while True:
    try:
        income_amount = float(income)
        break
    except ValueError:
        print(f'Invalid input: {income}.')
        income = input('Enter income amount, amount must be numeric: ')

while True:
    category = input('Enter category: ')
    if category == '':
        print(f'Invalid input: {category}.')
    elif not category.isalpha():
        print(f'Invalid input: {category}.')
    else:
        break

while True:
    income_date = input('Enter income date in (YYYY-MM-DD): ')
    try:
        income_dat = datetime.strptime(income_date, '%Y-%m-%d').date()
        break
    except ValueError:
        print(f'Invalid input: {income_date}.')
    # if income_date == '':
    #     print(f'Invalid input: {income_date}.')
    # elif not income_date.isnumeric():
    #     print(f'Invalid input: {income_date}.')
    # else:
    #     break