# ===============================================================
# Video Follow Along: Day 9 - casting
# ===============================================================
# This contains code snippets I create as I follow the video

myScore = int(input("Your score: "))
if myScore > 100000:
    print("Winner!")
else:
    print("Try again")

myPi = float(input("what is Pi to 3 dp: "))
if myPi == 3.142:
    print("Exactly!!")
else:
    print("Sorry, that is not quite right")
# ===============================================================
# Video Day 9 Challenge: casting
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("Generation identifier")
print()
year = int(input("Which year were you born: "))
if year >=1883 and year <= 1900:
    print("you are form the 'Lost Generation'")
elif year >= 1901 and year <= 1927:
    print("you are from the 'Greatest Generation'")
elif year >= 1928 and year <= 1945:
    print("you are from the 'Silent Generation'")
elif year >= 1946 and year <= 1964:
    print("you are from the 'Baby Boomer Generation'")
elif year >= 1965 and year <= 1980:
    print("you are from 'Generation X'")
elif year >= 1981 and year <= 1996:
    print("you are a 'Millenial'")
elif year >= 1997 and year <= 2012:
    print("you are from 'Generation Z'")
elif year >= 2013 and year <= 2025:
    print("you are from 'Generation Alpha'")
else:
    print("please enter a valid year")

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

#Program 11
print("Number identifier")
print()
number = int(input("please enter your number: "))
if number < 0:
    print(f"The number you have entered ({number}) is negative")
elif number == 0:
    print(f"the number you have entered ({number}) is neither positive nor zero it's zero")
elif number > 0:
    print(f"the number you have entered ({number}) is positive")
else:
    print("please enter a valid number")

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# 1) Option 3
# 2) Option 2
# 3) Option 1
# 4) floats (decimal numbers), integers (Whole numbers) and strings(Words/letters)
# 5) I would use a string as a name is compromised of multiple letters and no numbers
# 6) integers as the number of students is a whole number not a decimal
# 7) float as pi is a decimal number not a whole number
