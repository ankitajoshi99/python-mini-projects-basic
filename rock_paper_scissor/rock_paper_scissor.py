import random

user_win = 0
computer_win = 0

options = ['rock','paper','scissors']

while True:
     computer_input = random.choice(options)
     # random_number = random.randint(0,2)
     #computer_input = options[random_number]
     user_input = input("Type Rock/Paper/Scissors? or press Q to quit  ").lower()
     if user_input == 'q':
         print("You have quit the game  ")
         break
     if user_input not in options:
         print("Please select a valid option - Rock/Paper/Scissors or Q to quit ")
         continue
     if user_input == "rock" and computer_input == 'scissors':
         print("You win")
         print(f"Computer picked {computer_input}")
         user_win += 1
     elif user_input == 'paper' and computer_input == 'rock':
         print("You win")
         print(f"Computer picked {computer_input}")
         user_win += 1
     elif user_input == 'scissors' and computer_input == 'paper':
         print("You win")
         print(f"Computer picked {computer_input}")
         user_win += 1
     elif user_input == computer_input:
         print("Same option picked! ")
         print(f"Computer picked : {computer_input}, You picked : {user_input}")
     else:
         print("Computer wins!")
         print(f"Computer picked {computer_input}")
         computer_win += 1

print(f"Computer score is {computer_win} and User score is {user_win} ")
