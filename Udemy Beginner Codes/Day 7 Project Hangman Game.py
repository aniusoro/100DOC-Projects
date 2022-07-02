import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["america", "tiger", "camel", "edmonton", "nigeria", "apple", "laptop", "arsenal", "toronto", "plantain"]
#randomly select a word from worl_list
chosen_word = random.choice(word_list)

#testing code
# print(f"The chosen word is {chosen_word}")

#opening an empty list to store the '_'
display = []
for _ in range(len(chosen_word)):
    #making sure the amount of '_' is the same as the amount of  letters in chosen word
    display += "_"

#setting game over to false until the game actually ends
game_over = False
lives = 6
print(display)
#loop runs until game over
while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        #checking if the letter at 'position' is the same as teh guess given by the user
        if letter == guess:
            #if it is, we put that guess in the corresponding location in our 'display' list
            display[position] = letter
    if guess not in chosen_word:
      lives -= 1
    else:
      lives += 0
    

    print (display)

   
    if lives == 6:
      print(stages[6])
    elif lives == 5:
      print(stages[5])
    elif lives == 4:
      print(stages[4])
    elif lives == 3:
      print(stages[3])
    elif lives == 2:
      print(stages[2])
    elif lives == 1:
      print(stages[1])
    elif lives == 0:
      print(stages[0])

#when there are no more '_' in the 'display' list
    if "_" not in display or lives == 0:
        #the game is now over
            game_over = True
    if "_" not in display:
      print("You win")
    elif lives == 0:
      print(f"You lose, the word is {chosen_word}")
