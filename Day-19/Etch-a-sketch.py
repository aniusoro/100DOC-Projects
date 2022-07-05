"""
    the program below is an Etch-a-Sketch game
    this is a childhood game that I played that allows the user to make drawings
    based on the path of the turtle.
    the 'w' key is to move forward 10 steps
    the 's' key is to move backward 10 steps
    the 'd' key is to move right by 10 degrees
    the 's' key is to move left by 10 degrees
"""

from turtle import Turtle, Screen

ani = Turtle()
screen = Screen()


def move_forwards():
    ani.forward(10)


def move_backwards():
    ani.backward(10)


def turn_anticlockwise():
    ani.left(10)


def turn_clockwise():
    ani.right(10)


"""
    'ani.clear' deletes the turtle's drawings from the screen
    'ani.home' returns the turtle back to origin (0,0)
"""


def clear():
    ani.clear()
    ani.penup()
    ani.home()
    ani.pendown()


screen.listen()
""" the onkey method allows you to take input from keys on the keyboard
    it takes two parameters which are the key and a function
    when putting the function as a parameter, do not include the bracket   
"""
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_anticlockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key = "c", fun=clear)
clear()

screen.exitonclick()
