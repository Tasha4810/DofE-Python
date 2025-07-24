# ===============================================================
# Video Follow Along: Day 32 - lists
# ===============================================================
# This contains code snippets I create as I follow the video

timetable = ["Computer science","Mathematics","English","Art","Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
print()

timetable[4] = "science"
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])

print()
for lesson in timetable:
    print(lesson)

# ===============================================================
# Video Day 32 Challenge: lists
# ===============================================================
# This contains the code I created for the challenged posed in the video

import random
greetings = ["Hello!","konnichiwa!","Guten Tag!","Bore Da!","Bonjour","Hola","Halo","Γειά σου","привет","Ciao","cześć","haileo","Hei"]
index = random.randint(0,12)
print(greetings[index])

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

# Program 15
fav_films = ["Anastasia","Aristocats","Hercules","Seven Brides For Seven Brothers","The Land Before Time","The Lost City Of Atlantis","Treasure planet"]
print(f"{fav_films[2]} and {fav_films[4]}")

# Program 16
example_list = ["apples","bananas"]
random = ["hey",3,102.45,example_list]
for data in random:
    print(data)

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


