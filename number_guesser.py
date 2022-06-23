import random
# Make a random number
minimum_number = 0
maximum_number = 500
number = random.randrange(minimum_number,maximum_number)
# ^ This will generate a number between 0 and 500
answer_count = 0
# Next line is explaining the game and asking for a number to initialize
answer = int(input("I have generated a number between {} and {}, lets try to guess it! Type a number here and i will tell you if its higher or lower, lets start! ".format(minimum_number,maximum_number)))
answer_count += 1
# While loop to check the value
while answer != number:
    answer_count += 1
    if answer > number:
        answer = int(input(("Lower ")))
    else:
        answer = int(input(("Higher ")))
if answer == number:
    print("Congratulations! You've guessed the number in {} tries!".format(answer_count))