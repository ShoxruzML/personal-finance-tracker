# a CLI Personal Finance Tracker
import json
from datetime import datetime



def main():
    try:
        with open('transactions.json', 'r', encoding='utf-8') as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []
        print('transactions.json not found. Starting fresh.')
    print('*** PERSONAL FINANCE TRACKER ***')
    while True:
        user_input = input('Enter type (income/expense) or q to quit: ').lower()
        if user_input == 'q':
            print('*** QUITTING ***')
            break

        elif user_input == 'income':
            amount = input('Enter income amount: ')
            while True:
                        try:
                            amount = float(amount)
                            break
                        except ValueError:
                            print(f'Invalid input: {amount}.')
                            amount = input('Enter income amount, amount must be numeric: ')

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
                            income_date = datetime.strptime(income_date, '%Y-%m-%d').date()
                            income_date = income_date.isoformat()
                            break
                        except ValueError:
                            print(f'Invalid input: {income_date}.')
            entry = {
                'type': user_input,
                'amount': amount,
                'category': category,
                'date': income_date
            }
            transactions.append(entry)
        elif user_input == 'expense':
            expense_amount = input('Enter expense amount: ')
            while True:
                try:
                    expense_amount = float(expense_amount)
                    break
                except ValueError:
                    print(f'Invalid input: {expense_amount}.')
                    expense_amount = input('Enter expense amount, amount must be numeric: ')
            while True:
                category = input('Enter category: ')
                if category == '':
                    print(f'Invalid input: {category}.')
                elif not category.isalpha():
                    print(f'Invalid input: {category}.')
                else:
                    break

            while True:
                expense_date = input('Enter expanse date in (YYYY-MM-DD): ')
                try:
                    expense_date = datetime.strptime(expense_date, '%Y-%m-%d').date()
                    expense_date = expense_date.isoformat()
                    break
                except ValueError:
                    print(f'Invalid input: {expense_date}.')
            entry2 = {
                'type': user_input,
                'amount': expense_amount,
                'category': category,
                'date': expense_date
            }
            transactions.append(entry2)
        else:
            print(f'Invalid input: {user_input}.')


    with open('transactions.json', 'w', newline='', encoding='utf-8') as f:
        json.dump(transactions, f, indent=4, default=str, ensure_ascii=False)

    total_in = sum(t['amount'] for t in transactions if t['type'] == 'income')
    total_exp = sum(t['amount'] for t in transactions if t['type'] == 'expense')
    balance = total_in-total_exp
    category_totals = {}
    for t in transactions:
        if t['type'] == 'expense':
            cat = t['category']
            if cat not in category_totals:
                category_totals[cat] = 0
            category_totals[cat] += t['amount']

    biggest_category = max(category_totals, key=category_totals.get)
    print(f'Total in: ${total_in}')
    print(f'Total exp: ${total_exp}')
    print(f'Total balance: ${balance}')
    print(f'The biggest category is {biggest_category} (${category_totals[biggest_category]} expense).')
if __name__  == '__main__':
    main()