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
images = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors:\n "))


if player_input >= 3 or player_input < 0:
  print("You made a wrong choice. You lose!")
  exit()
print()
print("Your choice:")
print(images[player_input])

computer_choice = random.randint(0, 2)
print("Computer choice:")
print(images[computer_choice])
print()
if player_input == computer_choice:
  print("It's a tie")
elif computer_choice == 0 and player_input == 2:
  print("You lose!")
elif player_input == 0 and computer_choice == 2:
  print("you win!")
elif player_input > computer_choice:
  print("You win")
elif computer_choice > player_input:
  print("You lose!")
