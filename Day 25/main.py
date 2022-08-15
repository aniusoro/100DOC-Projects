import turtle
import csv
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 states correct", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

states_to_learn = list(set(all_states) - set(correct_guesses))

data_dict = {"states": states_to_learn}
data = pandas.DataFrame(data_dict)
data.to_csv("states_to_learn.csv")

screen.exitonclick()
