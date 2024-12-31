"""

Draw a triangle,square,pentagon,hexagon,heptagon,octagon, nonagon and decagon

"""
from turtle import *   # this imports everything
from turtle import Turtle,Screen
import random
import turtle as t
# (If typing “turtle” over and over again becomes tedious, use for example import turtle as t instead.)

timmy = Turtle()
# timmy.color('blue')  # changing the colour of the cursor or turtle
# timmy.width(3)  # changing the thickness or width of turtle
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(90)
# timmy.home()  # sending the turtle back home


# this is copies from chatgpt
colors = [
    "alice blue", "antique white", "aquamarine", "azure",
    "beige", "bisque", "black", "blanched almond", "blue",
    "blue violet", "brown", "burlywood", "cadet blue",
    "chartreuse", "chocolate", "coral", "cornflower blue",
    "cornsilk", "crimson", "cyan", "dark blue", "dark cyan",
    "dark goldenrod", "dark gray", "dark green", "dark khaki",
    "dark magenta", "dark olive green", "dark orange",
    "dark orchid", "dark red", "dark salmon", "dark sea green",
    "dark slate blue", "dark slate gray", "dark turquoise",
    "dark violet", "deep pink", "deep sky blue", "dim gray",
    "dodger blue", "firebrick", "floral white", "forest green",
    "fuchsia", "gainsboro", "ghost white", "gold", "goldenrod",
    "gray", "green", "green yellow", "honeydew", "hot pink",
    "indian red", "indigo", "ivory", "khaki", "lavender",
    "lavender blush", "lawn green", "lemon chiffon",
    "light blue", "light coral", "light cyan",
    "light goldenrod yellow", "light green", "light gray",
    "light pink", "light salmon", "light sea green",
    "light sky blue", "light slate gray", "light steel blue",
    "light yellow", "lime", "lime green", "linen", "magenta",
    "maroon", "medium aquamarine", "medium blue",
    "medium orchid", "medium purple", "medium sea green",
    "medium slate blue", "medium spring green",
    "medium turquoise", "medium violet red", "midnight blue",
    "mint cream", "misty rose", "moccasin", "navajo white",
    "navy", "old lace", "olive", "olive drab", "orange",
    "orange red", "orchid", "pale goldenrod", "pale green",
    "pale turquoise", "pale violet red", "papaya whip",
    "peach puff", "peru", "pink", "plum", "powder blue",
    "purple", "red", "rosy brown", "royal blue", "saddle brown",
    "salmon", "sandy brown", "sea green", "seashell", "sienna",
    "silver", "sky blue", "slate blue", "slate gray",
    "snow", "spring green", "steel blue", "tan", "teal",
    "thistle", "tomato", "turquoise", "violet", "wheat",
    "white", "white smoke", "yellow", "yellow green"
]

def draw_shape(no_sides):
    angle = 360 / no_sides # this gives us the angle based on which every side will rotate
    for _ in range(no_sides):
        timmy.forward(100)
        timmy.right(angle)

for change_side_n in range(3,11): # every shape has different number of sides so we pass each side of every shape
    timmy.color(random.choice(colors))
    draw_shape(change_side_n)


# screen = Screen()
# screen.exitonclick()