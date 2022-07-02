#Password Generator Project
#this creates a password for the user using a specified number of letters, numbers and symbols
import random
#this is the pool that the program will choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n")) 
number_of_symbols = int(input(f"How many symbols would you like?\n"))
number_of_numbers = int(input(f"How many numbers would you like?\n"))

#picks the specified amount of letters, symbols and numbers and assigns them to a list
letters_selected = random.choices(letters, k = number_of_letters)
symbols_selected = random.choices(symbols, k = number_of_symbols)
numbers_selected = random.choices(numbers, k = number_of_numbers)

#this is a function that converts a list to a string, that will be used later in the code
def list_to_string(list_to_convert):
    string = ""
    for element in list_to_convert:
        string += element
    return string

#creating an empty list
password_list = []
#appending the randomly selected letters to password_list
for x in letters_selected:
    password_list.append(x)
for y in symbols_selected:
    password_list.append(y)
for z in numbers_selected:
    password_list.append(z)
#doing a random shuffle of the list
random.shuffle(password_list)

#using the list_to_string function to convert password_list to a string and assigning that to password
password = list_to_string(password_list)
print (password)




