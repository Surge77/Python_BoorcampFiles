from turtle import Turtle,Screen

timmy = Turtle()  # object created of turtle stored timmy

screen = Screen()  # object created for screen

# to draw a simple square with the help of turtle graphics
# timmy.back(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
#
#
# screen.exitonclick()  # exits the windows when we tap once

# Different ways of importing modules

# by simply using import keyword and module name
# second method is by using from moduleName import Turtle,this imports specific class so that we don't have to
# repeatedly
# mention turtle name
# third method is importing everything using * like import random import * this will import everything
# fourth method is aliasing the module like import random as t
# here t will be represented as our module and while creating objects, we use this in case of long module names
# so when creating objects it becomes easy if we give our own custom name to the module