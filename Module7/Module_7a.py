# ===============================================================
# Video Follow Along: Day 48 - saving files
# ===============================================================
# This contains code snippets I create as I follow the video

f = open("savedFile.txt","w")
f.write("Hello there")
f.close()

f = open("savedFile.txt","a+")
WhatText = input("> ")
f.write(f"{WhatText}\n")
f.close()

# ===============================================================
# Video Day 48 Challenge: saving files
# ===============================================================
# This contains the code I created for the challenged posed in the video

#import os, time

#while True:
# print("HIGH SCORE TABLE")
# print()
# name = input("INITIALS > ").upper()
# score = input("SCORE > ")
# print()

# f  = open("high.score","a+")
# f.write(f"{name} {score}\n")
# f.close()

# print("ADDED")
# time.sleep(1)
# os.system("clear")

# The 'clear' doesn't seem to work. not sure why :(
# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

# Program 17

while True:
    print("FAVOURITE ANIMALS")
    print()
    fav_animals = input("Please enter your top 5 favourite animals\n >").capitalize()

    f = open("fav_animals.txt","a+")
    f.write(f"{fav_animals}\n")
    f.close()

    exit_animals_list = input("Is that all? (Y/N) : ").upper()
    if exit_animals_list == "Y":
        exit()
    else:
        continue

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


