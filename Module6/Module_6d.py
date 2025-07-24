# ===============================================================
# Video Follow Along: Day 25 - return
# ===============================================================
# This contains code snippets I create as I follow the video

def pin_picker(number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0, 9))
    return pin

my_pin = pin_picker(4)
print(my_pin)

def area_of_triangles(base,height):
    area = 0.5 * base * height
    return area

area = area_of_triangles(5,22)
print(area)
print()
print()
# ===============================================================
# Video Day 25 Challenge: return
# ===============================================================
# This contains the code I created for the challenged posed in the video
import random
print("--~<CHARACTER STAT GENERATOR>~--")


def char_health(six_side, eight_side):
    char_health = six_side * eight_side
    return char_health
name = input("Name your warrior: ")
char_health = char_health(random.randint(1,6), random.randint(1,8))
print(f"Their health is {char_health}")
# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# 1 - allow the programmer to break up the code into more manageable pieces and makes the code easier to read and understand
# 2 -makes the value available to be re-called
# 3 - the name of the function in the code is greeting and the argument is person_to_greet
