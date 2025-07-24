# ===============================================================
# Video Follow Along: Day 22 - libraries
# ===============================================================
# This contains code snippets I create as I follow the video

import random

my_number = random.randint(1, 100)
for i in range(10):
    print(my_number)

my_number = random.randint(1, 100)
print(my_number)

for i in range(10):
    my_number = random.randint(1, 100)
    print(my_number)

# ===============================================================
# Video Day 1 Challenge: libraries
# ===============================================================
# This contains the code I created for the challenged posed in the video

import random

mystery_number = random.randint(1, 1000000)
print("One-Million-To-One")
print()
counter = 1
while True:
    guess = int(input("What is your guess?: "))
    if guess == mystery_number:
        print("Well done you have guessed the number")
        print(f"It only took you {counter} attempts ")
        exit = input("Do you want to play again (Y/N)")
        if exit == "Y":
            continue
        elif exit == "N":
            break
        else:
            print(0)
    elif guess > mystery_number:
        print("Your guess is too high ")
        print("Try again")
        counter += 1
    elif guess < mystery_number and guess > 0:
        print("Your guess is too low ")
        print("Try again")
        counter += 1
    else:
        exit()


# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


