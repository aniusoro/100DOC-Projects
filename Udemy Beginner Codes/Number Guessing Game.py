import random

'''this is the function where the whole game is played'''
def guessing_game():
    print ("Welcome to the Number Guessing Game!")
    print ("I am thinking of a number between 1 and 100")

#answer is any number between 1 and 100 inclusive
    answer = random.randint(1,101)

    chances = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        chances = 10
    else: 
        chances = 5

#this was just a safety blanket for code testing. 
#    print(answer)
    game_over = False #this will be false until game ending conditons are met
    while not game_over:
        guess = int(input("Make a guess: "))
        if guess < answer:
            print("Too Low.\nGuess again.")
            chances -= 1
            print(f"You have {chances} attempts to guess the number.")
        elif guess > answer:
            print("Too High.\nGuess again.")
            chances -= 1
            print(f"You have {chances} attempts to guess the number.")
        else:
            print(f"You got it! The answer is {answer}")
            game_over = True

        if chances == 0:
            game_over = True
            print(f"You ran out of chances, the number is {answer}")

guessing_game()
play_again = input("Do you want to play again? ['Yes' / 'No']: ")
if play_again == "Yes":
    guessing_game()
else:
    print("Thanks, see you later!")

