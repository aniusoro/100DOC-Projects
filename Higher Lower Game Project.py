import random
from Higher_Lower_game_data import data



def generator():
    return random.choice(data)


def personality(account):
    name = account["name"]
    # followers = account["follower_count"]
    description = account["description"]
    nationality = account["country"]
    return (f"{name} is a {description} from {nationality}")

def Higher_Lower_Game():
    print("Welcome to the Higher Lower Game!")

# this generates the first instgram account + their bio 
    A = generator()
    A_bio = personality(A)
    print (A_bio)

# this generates the second instgram account to be compared + their bio 
    B = generator()
    B_bio = personality(B)
    print (B_bio)

#setting this initially to false
    game_over = False
#score starts at 0 and increases by 1 upon every correct entry
    score = 0
#until the game is over
    while not game_over:
        answer = input(f"Does {A['name']} have more/less instagram followers than {B['name']}?: enter [more / less]\n")
        X = A["follower_count"] > B["follower_count"]
        if X is True and answer == "more":
            score += 1
            print(f"Yes, your score is {score}")
            B = A
            A = generator()
            A_bio = personality(A)
            print (A_bio)
        elif X is False and answer == "less": 
            score += 1
            print(f"Yes, your score is {score}")
            B = A
            A = generator()
            A_bio = personality(A)
            print (A_bio)
        else:
            #game is over when they guess wrongly
            game_over = True
            print(f"No. Game Over!\nYour score is {score}")


    Play_Again = input("The Game is over, would you like to play again?\nEnter [Yes / No]")
    if Play_Again == "Yes":
        #function calls itself when the user wants to play again. 
        Higher_Lower_Game()
    else:
        print("Okay, see you next time!")


Higher_Lower_Game()