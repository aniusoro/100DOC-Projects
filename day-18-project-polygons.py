from turtle import Turtle, Screen
import random
"""using from turtle import * imports everything from the module"""

timmy = Turtle()
timmy.shape("arrow")

colors = ["green", "red", "blue", "pink", "DarkGreen"]
sides = 3

draw = True
while draw:
    the_color = random.choice(colors)
    for i in range(sides):
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)
    sides += 1
    timmy.color(the_color)
    if sides == 12:
        draw = False


# for i in range(sides):
#     timmy.forward(100)
#     timmy.right(90)
# sides += 1
#
# for i in range(sides):
#     timmy.forward(100)
#     timmy.right(72)


















screen = Screen()
screen.exitonclick()