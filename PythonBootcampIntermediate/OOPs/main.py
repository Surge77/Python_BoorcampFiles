
import turtle  # this is a module for turtle graphics

from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrange3")
#
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.right(120)
# timmy.forward(100)
# timmy.backward(120)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# print(my_screen.canvwidth)
# my_screen.exitonclick()

from prettytable import PrettyTable
#creating a table with the help of prettytable package and PrettyTable class

# columns = ["Pokemon Name", "Type"] #CREATES HEADER FOR THE COLUMNS
# table = PrettyTable()
#
# table.add_column(columns[0],["Pikachu", "Squirtle", "Charmander"]) #elements of first column
# table.add_column(columns[1],["Electric","Water","Fire"])  #elements of second column

table = PrettyTable()

#alternative way of doing

table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])

table.align = "r" # l => left align , r => right align , c => centre align
print(table)

