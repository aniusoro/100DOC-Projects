""" The program below creates a Kanye west  quote interface.
    I get the quotes from a Kanye rest API
"""

from tkinter import *
import requests


def get_quote():
    """ using a get() request to the Kanye Rest API"""
    quote = requests.get(url="http://api.kanye.rest")
    """ raising an exception if the request returned an unsuccessful status code"""
    quote.raise_for_status()
    """ parsing the JSON to obtain the quote request """
    data = quote.json()
    quote = data["quote"]
    """ then changing the canvas widget"""
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
