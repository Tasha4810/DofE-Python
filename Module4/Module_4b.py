# ===============================================================
# Video Follow Along: Day 15 - loops
# ===============================================================
# This contains code snippets I create as I follow the video

counter = 0
while counter <= 100:
    print(counter)
    counter += 1

exit = " "
while exit != "yes":
    print("Bye :)")
    exit = input("Exit?: ")

# ===============================================================
# Video Day 15 Challenge: loops
# ===============================================================
# This contains the code I created for the challenged posed in the video

exit = " "
while exit != "yes":
    animal = input("What animal do you want? : ")
    if animal == "cow":
        print("A cow goes moo")
        exit = input("Do you want to exit? : ")
    if animal == "Lesser Spotted Lemur":
        print("Umm... the lesser spotted lemur goes Awooga?")
        exit = input("Do you want to exit? : ")
    if animal == "dog":
        print("A dog goes woof")
        exit = input("Do you want to exit? : ")
    if animal == "cat":
        print("A cat goes Meow")
        exit = input("Do you want to exit? : ")
    if animal == "sheep":
        print("A sheep goes baaa")
        exit = input("Do you want to exit? : ")
    if animal == "chicken":
        print("A chicken goes cluck")
        exit = input("Do you want to exit? :")
print("You have ended the program if you wish to play again re run the program.")

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

number = int(input("please enter a positive number: "))
counter = 1
if number < 0:
    print("try again and Please enter a positive number")
else:
    while counter <= number:
        print(counter)
        counter += 1

number = int(input("Please can you enter a number between 1 and 10: "))
guess_number = int(input("Please enter a number between 1 and 10 as your guess: "))
if guess_number == number:
    print("Well done you have guessed the number correctly")
else:
    print("Your guess is not quite right, Please try again")

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


