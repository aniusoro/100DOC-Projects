from turtle import Turtle, Screen
import random
"""using from turtle import * imports everything from the module"""

timmy = Turtle()
timmy.shape("arrow")

"""the list of colors that the shapes will have their color randomly selected from"""
colors = ["green", "red", "blue", "pink", "DarkGreen"]

#starting with a triangle, the starting number of sides is 3
sides = 3

#this will mark the start and end of the drawing process
draw = True
while draw:
    the_color = random.choice(colors)
    for i in range(sides):
        angle = 360 / sides
        timmy.forward(100)
        timmy.right(angle)
        
    #increases the number of sides by 1 after a shape has been drawn
    sides += 1
    #the color is then changed
    timmy.color(the_color)
    #once the number of sides reaches 12, the while loop will end
    if sides == 12:
    #the loop will end when this is true
        draw = False


screen = Screen()
screen.exitonclick()
