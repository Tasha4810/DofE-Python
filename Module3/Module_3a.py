# ===============================================================
# Video Follow Along: Day 5 - if and else statements
# ===============================================================
# This contains code snippets I create as I follow the video
name = input("what's your name: ")
if name == "David" or name == "david":
    print("Welcome back David")
    print("you're the baldest dude I've ever seen")
else:
    print("who on earth are you?!")

name = input("what's your name: ")
if name == "Natasha" or name == "natasha":
    print("Welcome back Natasha")
    print("you're the coolest person I've ever known")
else:
    print("Stay away from the cool kids stuff")

# ===============================================================
# Video Day 5 Challenge: Statement of Intent Challenge
# ===============================================================
# This contains the code I created for the challenged posed in the video

# characteristics quiz ducktales
webby = input("are you good at martial arts: ")
if webby == "yes" or webby == "Yes":
    print("you are such a webby")
else:
    print("So you are not a webby")
huey = input("did you go to and enjoy boy scouts or brownies: ")
if huey == "yes" or huey == "Yes":
    print("you are such a huey")
else:
    print("So you are so not a huey")
dewey = input("are you adventurous and all about the action: ")
if dewey == "yes" or dewey == "Yes":
    print("you are such a dewey")
else:
    print("you are so not a dewey")
louie = input(" are you obsessed with wealth and money: ")
if louie == "yes" or louie == "Yes":
    print("you are such a dewey")
else:
    print("you are so not a louie")




# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

#Program 9
print("I am going to ask for your favourite food can you type it in when asked"
      " make sure the second player doesnt see it")
fav_food = input("Please type in your favourite food: ")
guess = input("Can you guess what my favourite meal is: ")
if guess == fav_food:
    print("Well done you guessed correctly")
else:
    print("Nice try, but you guessed incorrectly")

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# --- James ---
# Now we're getting into the real stuff! If statements are the backbone of coding.
# One change I would make to the Programme above is to add a small amount of handling for things like upper and lower cases.
# This just avoids the fav_food being "rice" and the guess being "Rice" and this being interpreted as a wrong answer.
# Here's a small example:
print("I am going to ask you for your favourite type of music. Then the next player is going to guess and see how well they know you.")
music = input("Tasha, what is your favourite genre of music?: ")
guess = input("Thanks, now Donal.\nWhat would you say is Tasha's favourite genre of music?: ")
if music.lower() == guess.lower():
    print("Donal knows you really well!")
else:
    print("You hardly even know your own daughter. :(")

# --- NATASHA ---
# Ok James good to know. I think in later programs I have included both the upper and lower case versions but this would probably
# work better and be easier for me to use. :)

