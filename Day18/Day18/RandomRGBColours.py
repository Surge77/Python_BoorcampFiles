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
    random_colour = (r,g,b)
    return random_colour


for _ in range(200):
    timmy.width(10) # changes thickness of cursor
    timmy.speed("fast") # changes the speed of the cursor we can either change it through string or integer
    # 0 - fastest  "fast" - 10  "normal" - 6 slowest - 1   "slow" - 3
    timmy.color(random_colour())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))