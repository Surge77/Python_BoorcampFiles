"""

Higher Order Functions in python

A function that is having another function as an argument or a function that returns another function as
a return in the output is called the High order function. High order functions operate with other functions given in
the program.

In this we will also learn about turtle events and different methods associated with it

"""
from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

screen.listen()
# the method listens to even like space and moves turtle forward by 10 places
screen.onkey(key="space", fun=move_forward)  # this is a concept of high er order function
screen.exitonclick()