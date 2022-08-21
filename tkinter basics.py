from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
# adding space around the program
window.config(padx=100, pady=200)
# Label
my_label = Label(text="Ani was here", font=("Arial", 24, "bold"))
# use this to change the text property
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
# any widget without a layout manager (i.e. pack, place, grid) will not be shown
# you have to choose one layout manager throughout your code
# my_label.pack()
# my_label.place(x=0, y=0)

# Buttons
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)
button2 = Button(text="new button", command=button_clicked)
button2.grid(column=2, row=0)

# Entry
input = Entry()
print(input.get())
input.grid(column=3, row=2)





# should always be at the very end
window.mainloop()
