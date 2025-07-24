# ===============================================================
# Video Follow Along: Day 24 - Parameters
# ===============================================================
# This contains code snippets I create as I follow the video

def which_cake(ingredient, base, coating):
    if ingredient == "red velvet":
        print("Mmm red velvet cake is amazing")
    elif ingredient == "brocolli":
        print("you what mate?!")
    else:
        print("Yeah, that's great i suppose...")
    print(f"So you want a {ingredient} cake on a {base} base with {coating} on top?")
ingredients = input("Name an ingredient: ")
base = input("Name a base: ")
coating = input("Name a coating: ")
which_cake(ingredients, base, coating)

# ===============================================================
# Video Day 24 Challenge: parameters
# ===============================================================
# This contains the code I created for the challenged posed in the video
import random
print()
print()
def roll_dice(sides):
    dice = random.randint(1, sides)
    print(f"you rolled {dice}")

print("INFINTY DICE !!")
sides = int(input("How many sides?: "))
roll_dice(sides)

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


