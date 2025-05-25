# Quiz app is a basic python program.
# user is promoted to answer questions
# each right answer adds +1 to the score
# score is displayed at the end of the quiz along with the %

print('Welcome to the Python quiz.')
score = 0

quiz = input('Do you want to get started?  ')
if quiz.lower() != "yes":
    quit()

answer = input("What keyword is used to define a function in Python? ")
correct_ans = "def"
if answer == correct_ans:
    print("Correct!")
    score += 1
else:
    print(f"Incorrect!, the correct answer is {correct_ans}")

answer = input("Which function is used to get input from user?  ")
correct_ans = "input()"
if answer == correct_ans:
    print("Correct!")
    score += 1
else:
    print(f"Incorrect!, the correct answer is {correct_ans}")

answer = input("What function is used to convert a string to lowercase? ")
correct_ans = "lower()"
if answer == correct_ans:
    print("Correct!")
    score += 1
else:
    print(f"Incorrect!, the correct answer is {correct_ans}")


print(score)
print(f"Your score is {score} /3 ")
print(f"Your percentage is {(score/3) * 100:.2f} %")