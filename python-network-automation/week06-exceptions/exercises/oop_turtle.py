print('#' * 10 + ' OOP DEMO: THE TURTLE ' + '#' * 10)
# OOP DEMO: THE TURTLE
"""
Abstraction vs. Encapsulation

Abstraction: key concept in OOP, and its goal
is to handle complexity by hiding unnecessary
details from the user.

Encapsulation: mechanism of binding attributes and methods
together as a single unit. Also known as data hiding.
"""


from turtle import Turtle, Screen
my_screen = Screen()
donatello = Turtle()
print(my_screen.canvwidth)
donatello.shape('turtle')
donatello.color('purple')
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(100)
donatello.right(90)
donatello.forward(200)
donatello.home()

raphael = Turtle()
raphael.shape('turtle')
raphael.color('red')
raphael.penup()
raphael.goto(-150,200)
raphael.pendown()
raphael.pencolor('blue')

x =  10
while x <= 50:
    raphael.circle(x)
    donatello.circle(x+5)
    x += 10

my_screen.exitonclick()