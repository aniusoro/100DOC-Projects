import turtle
from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
"""setup allows us to set the width and height of our screen"""
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40, -10, 20, 50, 80]
all_turtles = []

"""this will display all the racing turtles at the start of the race track"""
for _ in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    """the goto method sends our turtle to a specific coordinate within our screen"""
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[_])
    all_turtles.append(new_turtle)

""" once the user gives a bet, then the race can begin
    if no input is given then the race will not begin
"""
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
# this marks when a turtle has crossed the finish line
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                #user wins if the bet is correct and loses if the bet is wrong
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()