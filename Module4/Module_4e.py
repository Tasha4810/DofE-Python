# ===============================================================
# Video Follow Along: Day 18 - Guessing game
# ===============================================================
# This contains code snippets I create as I follow the video

# a project video

# ===============================================================
# Video Day 18 Challenge: Guessing game
# ===============================================================
# This contains the code I created for the challenged posed in the video

# this is also the program to be assessed
mystery_number = int(input("Please enter a number between 1 and 1 million for the other person to guess:"))
print("One-Million-To-One")
print()
counter = 1
while True:
    guess = int(input("What is your guess?: "))
    if guess == mystery_number:
        print("Well done you have guessed the number")
        print(f"It only took you {counter} attempts ")
        break
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


