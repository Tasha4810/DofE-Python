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

# --- James ---
# I can see that you have done functions further up so am just going to say that this is a great opportunity to use a function to ensure that you get a correct input from you user
def return_valid_input(question, valid_response):
    """
    A function that will only return if a valid response is given.
    It has an internal timeout of 10 responses.
    :param question: string input to be posed
    :param valid_response: list of possible responses
    :return resp: response from the user
    """
    valid_input = False
    attempts = 0
    while not valid_input:
        resp = input(question)
        if resp in valid_response:
            valid_input = True
        attempts += 1
        print("    Invalid input, please re-enter")

    return resp

# Here is the same programme but using the above function to ensure that a number between 1 and 10 is entered.
# I have made it mre complicated by making the checking function general, so it has to be given a list from 1 to 10 to check against.
number = int(return_valid_input("Please can you enter a number between 1 and 10: ", [str(x) for x in range(0,10)]))
guess_number = int(return_valid_input("Please enter a number between 1 and 10 as your guess: ", [str(x) for x in range(0,10)]))
if guess_number == number:
    print("Well done you have guessed the number correctly")
else:
    print("Your guess is not quite right, Please try again")