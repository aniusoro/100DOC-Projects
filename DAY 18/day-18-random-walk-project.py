from turtle import Turtle
from turtle import Screen
import random


ani = Turtle()
ani.shape("arrow")
ani.pensize(10)
ani.speed("fastest")

counter = 0
keep_walking = True

while keep_walking:
    colors = ["red", "blue", "tomato", "sky blue", "IndianRed", "DarkOrchid"]
    ani.color(random.choice(colors))
    angles = [0, 90, 180, 270]
    ani.forward(30)
    ani.right(random.choice(angles))
    counter += 1
    if counter > 200:
        keep_walking = False
    else:
        keep_walking


screen = Screen()
screen.exitonclick()
