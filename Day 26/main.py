student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

file = pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dict = {row.letter:row.code for (index, row) in file.iterrows()}
print(NATO_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word:").upper()
output_list = [NATO_dict[letter] for letter in user_word]
print(output_list)

