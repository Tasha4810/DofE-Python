# ===============================================================
# Video Follow Along: Day 33 - Dynamic Lists
# ===============================================================
# This contains code snippets I create as I follow the video

my_agenda = []

def printlist():
    print()
    for item in my_agenda:
        print(item)
    print()

while True:
    menu = input("Add or remove?: ")
    if menu == "add":
        item = input("What's next on the agenda?: ")
        my_agenda.append(item)
        finished = input("Is the agenda finished? (Y/N): ")
        if finished == "Y":
            break
        elif finished == "N":
            continue
        else:
            break
    elif menu == "remove":
        finished = input("Is the agenda finished? (Y/N): ")
        if finished == "Y":
            break
        elif finished == "N":
            continue
        else:
            break
        item = input("What do you want to remove?: ")
        if item in my_agenda:
           my_agenda.remove(item)
        else:
            print(f"{item} was not in the agenda.")
printlist()


# ===============================================================
# Video Day 33 Challenge: Dynamic lists
# ===============================================================
# This contains the code I created for the challenged posed in the video

import os, time
to_do_list = []

def printlist():
    print()
    for item in to_do_list:
        print(item)
        print()

while True:
    menu = input("to do list manager \n Do you want to view, add or edit the to do list?\n")
    if menu == "view":
        printlist()
    elif menu == "add":
        item = input("What do you want to add?: ")
        to_do_list.append(item)
    elif menu == "edit":
        item = input("What do you want to remove?: ")
        if item in to_do_list:
            to_do_list.remove(item)


# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


