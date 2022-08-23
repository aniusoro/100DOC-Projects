from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

""" This is a program that creates an interface where a user can put in a website, email and password.
    The user can also have the luxury of having a password generated for them. 
    This can be done after clicking the 'generate password' button
    These pieces of data are then stores into a file called data.txt
    This program uses tkinter, message boxes, list comprehension, and a host of other lovely python features. 
"""
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
""" This is the function that does the password generation """
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


""" .join adds together all the lists that make up password_list"""
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    """ here if the user does not enter anything, a popup message will be displayed to let them know
        If they do enter all the required fields, they will have a confirmation pop-up.
        Their data is then stored onto the txt file.
    """
    entry1 = website_entry.get()
    entry2 = email_entry.get()
    entry3 = password_entry.get()

    if len(entry1) == 0 or len(entry3) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.😬")
    else:
        is_okay = messagebox.askokcancel(title=entry1, message=f"These are the details entered: \nWebsite: {entry1} \nEmail: {entry2}"
                                                               f"\nPassword: {entry3} \n Is it ok to save?")

        if is_okay:
            with open("data.txt", "a") as file:
                file.write(f"{entry1} | {entry2} | {entry3}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #


Font_name = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

"""  this is where all the interactive buttons and entries are created and configured to the programmers desire"""
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=38)

""" focus makes sure that the cursor is already displayed in the entry box"""
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
""" pre-populate the email entry with our preferred email"""
email_entry.insert(0, "akpanusohanietie@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
