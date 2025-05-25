import random

## Number Guessing Game
# A simple Python program where -
#  user is prompted to enter an upper limit (n), defining range from 0 to n.
#  with the given range, program generates a random number
#  user then tries to guess the random number ( within the retries/guesses user has chosen)
#  the program gives a hint whether the guess is greater or lesser than the random number for each guess
#  the game continues until the user has guessed correctly or runs out of allowed attempts.

range_of_number = (input("Enter a number (upper limit) to generate a random number from 0 to : "))
# Input from the user should be a positive integer
# "10" is being changed to 10
if range_of_number.isdigit():
    range_of_number = int(range_of_number)
else:
    print("Please type a positive number next time!")
    quit()
#Generating a random number from 0 to range, 0 and range included
random_number = random.randint(0,range_of_number)
guesses = 0
retry = int(input("How many guesses would you want ?"))

while True:
    guesses += 1
    guess_number = input("Guess the number!")
    if guess_number.isdigit():
         guess_number = int(guess_number)
    else:
        print("Please guess with a positive number next time")
        continue # Continue will prompt the user to guess again
    if guess_number == random_number:
        print(f"You got it right in {guesses} attempts!")
        break
    elif guess_number > random_number:
        print("Greater than the number")
    else:
        print("Lesser than the random number")
    if guesses >= retry:
        print("Your chances are over!")
        break
    else:
        print(f"You have {retry-guesses} tries left!")

if guesses == retry and guess_number != random_number:
    print(f"Game over! Random number is {random_number}")








