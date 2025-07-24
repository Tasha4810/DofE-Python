# ===============================================================
# Video Follow Along: Day 10 - a bit of math
# ===============================================================
# This contains code snippets I create as I follow the video

adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

squared = 5**2
print(squared)

modulo = 15 % 4
print(modulo)

divisor = 15 // 4
print(divisor)

mybill = float(input("what was the bill?: "))
numofpeople = int(input("how many people?: "))
answer = mybill / numofpeople
answer = round(answer, 2)
print(f"you all owe £{answer}")

# ===============================================================
# Video Day 10 Challenge: a bit of math
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("Tip calculator")
print()
billcost = float(input("How much did you spend?: "))
tip = int(input("What percentage would you like to tip?: "))
groupsize = int(input("How many people are in your group?: "))
tip = tip / 100
tip = billcost * tip
billcost = billcost + tip
owedpp = billcost / groupsize
owedpp = round(owedpp, 2)
if groupsize == 1:
    print(f"you owe £{owedpp} plus tip")
elif groupsize > 1:
    print(f"you each owe £{owedpp} plus tip")
else:
    print("can you please try again your groupsize is invalid")


# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================


