import random
import os

'''this is the function that will clear the screen after a round of the game has concluded'''
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

'''this function deals cards to the player and the AI'''
def deal_cards():
    '''returns a random card from the deck.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

'''this calculates each players score for their current hand'''
def hand_score(cards):
    '''returns the players score'''
    summation = 0
    for values in cards:
        summation += values
    if summation == 21 and len(cards) == 2:
        return 0
    if 11 in cards and summation > 21:
        cards.remove(11)
        cards.append(1)
    return summation

'''this function compares the player's score and the AI's score and returns who wins the game'''
def compare(Player_score, AI_score):
    if Player_score == AI_score:
        return "Draw"
    elif AI_score == 0:
        return "Lose, AI has a blackjack"
    elif Player_score == 0:
        return "Win with a blackjack"
    elif Player_score > 21:
        return "You went over, You lose"
    elif AI_score > 21:
        return "AI went over, You win"
    elif Player_score > AI_score:
        return "You win"
    else:
        return "You lose"

'''the game function'''
def Black_Jack_Game():
    
    Player_hand = []
    AI_hand = []
#this starts as false but when True, marks the end of the game
    game_over = False

    for _ in range(2):
        Player_hand.append(deal_cards())
        AI_hand.append(deal_cards())

    while not game_over:
        Player_score = hand_score(Player_hand)
        AI_score = hand_score(AI_hand)
        print(f"Your hand is {Player_hand}, current score is {Player_score}")
        print(f"AI's first card is {AI_hand[0]}")
    
#this is when either player has a black jack or the user has gone over 21
        if Player_score == 0 or AI_score == 0 or Player_score > 21:
            game_over = True
        else:
            deal_again = input("Type 'y' to enter another card, and 'n' to pass.\n")
            if deal_again == 'y':
                Player_hand.append(deal_cards())
            else:
                game_over = True
    
    while AI_score != 0 and AI_score < 17:
        AI_hand.append(deal_cards())
        AI_score = hand_score(AI_hand)

    print(f"Your final hand is {Player_hand} and your final score is {Player_score}")
    print(f"AI's final hand is {AI_hand} and its final score is {AI_score}")
    print(compare(Player_score, AI_score))
        
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clearConsole()
    Black_Jack_Game()
            


