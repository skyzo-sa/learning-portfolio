print('#' * 10 + ' PYTHON FLOW CONTROL ' + '#' * 10)
print('#' * 10 + ' CONDITIONAL STATEMENTS ' + '#' * 10)
# CONDITIONAL STATEMENTS

balance = 100
price = 50

if balance >= price:
    answer = input('Do you want to continue? Enter "yes" or "no": ')
    answer = answer.lower()
    if answer == 'yes':
        print('Good job! We\'ll move one.')
    elif answer == 'no':
        print('Good bye! We\'ll stop.')
    else:
        print('Invalid answer')
    new_balance = balance - price
    print(f'You can book the flight and your new balance is R{new_balance}')
else:
    print(f'Insufficient funds! Please deposit {price - balance}')

print('Other instructions ...')
x = 10
# ....



