# ===============================================================
# Video Follow Along: Day 19 - for loop
# ===============================================================
# This contains code snippets I create as I follow the video

counter = 0
while counter < 10:
    print(counter)
    counter += 1

for counter in range(10):
    print(counter)



# ===============================================================
# Video Day 19 Challenge: for loop
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("Loan Calculator")

loan_value = float(input("Please enter the loan amount: "))
time = int(input("For how many years will you keep the loan? "))
interest_rate = float(input("Please enter the annual interest rate (APR) in %: "))

original_loan = loan_value

print(f"1£{original_loan} over {time} years at {interest_rate}% APR\n")

for year in range(time):
    loan_value = loan_value * (1 + interest_rate / 100)
    loan_value = round(loan_value, 2)
    print(f"Year {year + 1}: £{loan_value}")

extra_paid = round(loan_value - original_loan, 2)
print(f"\nYou paid £{extra_paid} in interest.")


# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment



# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

#1) while - only run while a condition is true  for - only run for the amount of times allocated
#2)stops running a loop
#3)generates a sequence of number from 0 to less than the number????  <----- explain better
#4) for i in range(5):
#       print("Hello world")

# --- James ---
# For loops! God, they're great. Excited to see where we're going with this
