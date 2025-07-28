# ===============================================================
# Video Follow Along: Day 3 - concatenation
# ===============================================================
# This contains code snippets I create as I follow the video

# Program 1
name = input("what's your name?:")
lunch = input("what are you having for lunch?:")
print(name, "is going to be chowing down on" ,lunch, "very soon")

# Program 2
name = input("what's your name?:")
year = input("what year is it?:")
print(name, "thinks it is", year)

# ===============================================================
# Video Day 3 Challenge: Concatenation Challenge
# ===============================================================
# This contains the code I created for the challenged posed in the video

# food = input("name a food:")
# plant = input("name a plant: ")
# cooking = input("name a cooking method: ")
# adjective = input("what word could you use to describe burnt food?: ")
# item = input("name a household item: ")
# print( )
# print("MENU")
# print(cooking,food,"with",adjective,plant,"on a bed of",item)

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

# Program 6
name = input ("What's your name: ")
age = input("How old are you: ")
language = input("What's your favourite programming language: ")
print( )
print(f"""
So, your name is {name}, you are {age} years old and you really enjoy programming in {language}!""")

# Program 7
character = input("name a cartoon character :")
plant = input("name a plant :")
tool = input("name a DIY tool :")
print("your rockstar name is:",character,plant, tool)


# --- JAMES ---
# I've learned something again! Wasn't aware that you could just pass arguments into the print() function and it will concatenate them with nice spaces added. Very cool.
# I'm a big fan of the f"" notation for formatting strings as it makes it really clear how the variables are inserted into the text.
coder_name = "Natasha"
assesment = "great"
print(f"James thinks that {coder_name} is making {assesment} progress", "and", "wanted", "to", "test", "what", "she", "taught", "him", ".")
