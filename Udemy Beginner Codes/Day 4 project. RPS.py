import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_choice = input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n')
if player_choice == '0':
    print(rock)
elif player_choice == '1':
    print(paper)
elif player_choice == '2':
    print(scissors)
else:
    player_choice = input('wrong input, try again\n')
    if player_choice == '0':
        print(rock)
    elif player_choice == '1':
        print(paper)
    elif player_choice == '2':
        print(scissors)


AI_choice = random.randint(0,2)
AI_choice = str(AI_choice)
print(f"Computer chose: {AI_choice}") 
if AI_choice == '0':
    print(rock)
elif AI_choice == '1':
    print(paper)
elif AI_choice == '2':
    print(scissors)

if player_choice == AI_choice:
    print("This game is a draw")
elif ((player_choice == '0') and (AI_choice == '1')) or ((player_choice == '1') and (AI_choice == '2')) or ((player_choice == '2') and (AI_choice == '0')):
    print("You lose")
elif (player_choice == '0') and (AI_choice == '2') or ((player_choice == '1') and (AI_choice == '0')) or ((player_choice == '2') and (AI_choice == '1')):
    print("You win")
else:
    print("I dunno how, but there was no winner")

