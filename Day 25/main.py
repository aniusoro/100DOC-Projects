""" This is a program that serves as an educational game to help kids learn the states of the US
    When the pop-up dialogue comes, the user then types in the name of a state, if a real state
    then their score increases by one if not, they get to keep attempting
    When the user is tired of guessing and wants to end the game, they can type in "Exit" and end the game.
    
    After that, the states that the user does not get right are saved into a cvs file called "states_to_learn.cvs"
    which they can now learn afterwards. 

"""

"""importing the turtle, csv and pandas modules"""
import turtle
import csv
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
"""here I added the image of the US map as the image ti be displayed on the screen"""
screen.addshape(image)
turtle.shape(image)


""" this is the conversion of the cvs to a list """
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states correct", prompt="What's another state's name?").title()
    
""" 'Exit' breaks out of the loop """
    if answer_state == "Exit":
        break
""" The state when mentioned is then placed on the appropriate location on the map """
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

"""  this is where we make a list of states the user has to learn. """
states_to_learn = list(set(all_states) - set(correct_guesses))


""" this is where the states not mentioned are then made into a cvs for the user to learn. """
data_dict = {"states": states_to_learn}
data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")

screen.exitonclick()
