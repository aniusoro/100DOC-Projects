""" This is a program that creates a flashcard application.
    The flashcard helps the user to learn French words and their English translations.
"""


from tkinter import *
import csv
import pandas
from random import *


BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}
"""  we first try to see if the user is in a new session and has words to learn"""
try:
    data = pandas.read_csv("data/words_to_learn.csv")
    #   if it is a new session, we then open the French words file and convert it into a dictionary
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    #   if an old session we then just convert the words to learn to a dictionary
    to_learn = data.to_dict(orient="records")

"""
    this function displays the front of the next card which is the next french word to be learnt.
"""


def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


"""
    the flip_card function shows the english translation for the french word.
    In essence it flips to the back of the card
"""   


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    to_learn.remove(current_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

""" the 'window.after' function takes 2 arguments, which are the time in Milliseconds and a function
    here after 3 seconds (3000 milliseconds), we run the function known as flip_card
"""
flip_timer = window.after(3000, func=flip_card)

""" here I am creating the canvas and importing the images
    also, I am placing the captions and configuring them
"""
canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

""" this is where i convert the images on the canvas to buttons
"""
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

"""
    once the program is  up and running, the first word is displaced on the from immediately,
    once the function: next_card is called
"""
next_card()

window.mainloop()
