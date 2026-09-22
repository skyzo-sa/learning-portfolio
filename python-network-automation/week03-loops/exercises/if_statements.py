print('#' * 10 + ' if STATEMENTS ' + '#' * 10)

print('#' * 10 + ' CONDITIONAL STATEMENTS ' + '#' * 10)
# CONDITIONAL STATEMENTS
#
balance = 100
price = 500

if balance >= price:
    new_balance = balance - price
    print(f'You can book the flight and your new balance is R{new_balance}')
else:
    print(f'Insufficient funds! Please deposit {price - balance}')

print('Other instructions ...')
x = 10
# ....

print('#' * 10 + ' PYTHON FLOW CONTROL ' + '#' * 10)

answer = input('Do you want to continue? Enter "yes" or "no": ').lower()
if answer == 'yes':
    print('Good job! We\'ll move one.')
elif answer == 'no':
    print('Good bye! We\'ll stop.')
else:
    print('Invalid answer')


# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
#
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')