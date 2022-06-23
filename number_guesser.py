import random

# Make a random number
number = random.randrange(0,500)
print(number)
# This will generate a number between 0 and 500
answer_count = 1
answer = int(input("I have generated a number between 0 and 500, lets try to guess it! Type a number here and i will tell you if its higher or lower, lets start! "))

while answer != number:
    answer_count += 1
    if answer > number:
        answer = int(input(("Lower ")))
        continue
    else:
        answer = int(input(("Higher ")))
if answer == number:
    print("Congratulations! You've guessed the number in {} tries!".format(answer_count))