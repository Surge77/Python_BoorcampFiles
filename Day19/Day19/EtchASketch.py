"""

To make use of event listeners and higher order functions

Tasks:

The keys should do the following functions

W - Forwards
S - Backwards
A - counter-clockwise or turnleft
D - Clockwise or turn right
we need to create separate functions for these
C - clear drawing

"""

from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# the method listens to even like space and moves turtle forward by 10 places
screen.onkey(key="w", fun=move_forward)  # this is a concept of higher order function
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c",fun=clear)
clear()
screen.exitonclick()