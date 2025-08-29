# ===============================================================
# Video Follow Along: Day 49 - Reading a file
# ===============================================================
# This contains code snippets I create as I follow the video

f = open("high.score", "r")
contents = f.read ()
f.close()

contents = contents.split

print(contents)

f = open("fav_animals.txt", "r")
while True:
    contents = f.readline().strip()
    if contents == "":
        break
    print(contents)
f.close()

# ===============================================================
# Video Day 49 Challenge: Reading a file
# ===============================================================
# This contains the code I created for the challenged posed in the video

f = open("high.score", "r")
scores = f.read(). split("\n")
f.close()

high_score = 0
name = None

for lines in scores:
    data = lines.split()
    print(data)
    if data != []:
        if int(data[1]) > high_score:
            high_score = int(data[1])
            name = data[0]
print(f"The winner is {name} with a score of {high_score} congratulations!!!")

# ===============================================================
# Programs
# =================s))==============================================
# These are programs I create for assessment

# Program 18

f = open("fav_animals.txt", "r")
animals = f.read()
print((animal
f.close()

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# 1 it allows you to make any adjustments to the file and is useful for good data management.
# 2 writing in append mode is why you are adding something to a preexisting file.
# 3 the code will crash - not certain
