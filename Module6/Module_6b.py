# ===============================================================
# Video Follow Along: Day 1 - Print and the Workspace
# ===============================================================
# This contains code snippets I create as I follow the video

def roll_dice():
    import random
    dice = random.randint(1,6)
    print(f"you rolled {dice}")

for i in range(100):
    roll_dice()

def count_to_five():
    for i in range(1,6):
        print(i)

count_to_five()

# ===============================================================
# Video Day 1 Challenge: Statement of Intent Challenge
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("REPLIT LOGIN SYSTEM")

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "password123"

def login_loop():
    while True:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("Login successful. You are now logged in.")
        else:
            print("Incorrect username or password. Exiting login loop.")
            break

login_loop()


# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


