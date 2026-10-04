print('#' * 10 + ' OOP : MAGIC METHODS ' + '#' * 10)
# OOP : MAGIC METHODS

""" They're always surrounded by double underscores(__)
and they;re also called: special or dunder methods.

They're special or magic because you don't have to call them directly.
The invocation is automatically done by the Python interpreter behind the scenes. 
"""
class Robot:
    """ This class implements a robot """
    population = 0 # class attribute
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1

    def __del__(self):
        print('Robot destroyed!')

    def __str__(self):
        my_str = f'My name is {self.name} and my price is: {self.price}'
        return my_str

    def __add__(self, other):
        price = self.price + other.price
        return price

r1 = Robot('Marvin', 150)
r2 = Robot('Lucy', 45)
print(r1)
print(r1 + r2)



