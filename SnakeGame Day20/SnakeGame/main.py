from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("The Snake Game")

starting_positions = [(0,0),(-20,0),(-40,0)] # these are tuples in a list

# the starting position of a turtle is (0,0) as we move left we get negative co-ordinates

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)































screen.exitonclick()