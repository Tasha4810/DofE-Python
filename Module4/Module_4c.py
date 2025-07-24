# ===============================================================
# Video Follow Along: Day 16 - While true loop
# ===============================================================
# This contains code snippets I create as I follow the video

while True:
    print("This program is running")
    goAgain = input("Go again?:  ")
    if goAgain == "no":
        break
print("Aww, i was having a good time :( ")

# while true :
# repeat this code for infinity

# ===============================================================
# Video Day 16 Challenge: While True loop challenge
# ===============================================================
# This contains the code I created for the challenged posed in the video

counter = 0
while True:
    print("Never going to ______ you up ")
    guess = input("What lyric goes in the gap?:  ")
    counter += 1
    if guess == "give":
        if counter == 1:
            print("Well done you must know this song well it only took you 1 attempt")
            break
        else:
            print(f"Well done it only took you {counter} attempts")
            break
    else:
        print("Nope, try again")

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


