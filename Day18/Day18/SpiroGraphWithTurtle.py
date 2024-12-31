import turtle as t
import turtle
from turtle import *   # this imports everything
from turtle import Turtle,Screen
import random

# python Tuples and how to generate random rgb colours

timmy = Turtle()
directions = [0,90,120,270]
turtle.colormode(255)

def random_colour(): # this will create even more colors than defined previosly with rgb mixing
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r,g,b)
    return colour



timmy.speed("fastest") # changes the speed of the cursor we can either change it through string or integer
# 0 - fastest  "fast" - 10  "normal" - 6 slowest - 1   "slow" - 3

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_colour())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+10)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()
