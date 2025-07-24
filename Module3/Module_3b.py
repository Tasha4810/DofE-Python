# ===============================================================
# Video Follow Along: Day 6 - ELIF
# ===============================================================
# This contains code snippets I create as I follow the video

print("SECURE LOGIN")
username = input("username: ")
password = input("password: ")
if username == "mark" and password =="password":
    print("Welcome Mark!")
elif username == "suzanne" and password == "su7ann3":
    print("Hey there suzanne")
else:
    print("Go away!")


# ===============================================================
# Video Day 6 Challenge: Statement of Intent Challenge
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("MY LOGIN SYSTEM")
print( )
username = input("username: ")
password = input("password: ")
if username == "mark" and password =="totallynotbald":
    print(f"""
    why hello there {username}, what a lovely accent you have, you could have charmed your way in here without a password.
    
    Have a great day.
    Dont forget to wear a hat in the sun!
    """)
# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

print("ROCK PAPER SCISSORS")
game = input("would you like to play rock paper scissors: ")
if game == "yes" or game == "Yes":
    print("lets play")
    users_move = input("please enter your move: ")
    if users_move == "rock" or users_move == "Rock":
        print(" I win i chose paper")
        print("dont worry im sure you will win next time")
    elif users_move == "paper" or users_move == "Paper":
        print("i win i chose scissors")
        print("its alright you almost won try a little harder next time")
    elif users_move == "scissors" or users_move == "Scissors":
        print(" you lose i chose paper")
        print("oh dont cry its only a game of rock paper scissors you'll live through it")
    else:
        print("even though you tried to cheat i won anyways i chose the infinty gauntlet and have snapped you decision away leaving you defenceless")
# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

