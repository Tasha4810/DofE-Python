# ===============================================================
# Video Follow Along: Day 40 -
# ===============================================================
# This contains code snippets I create as I follow the video



# ===============================================================
# Video Day 40 Challenge:
# ===============================================================
# This contains the code I created for the challenged posed in the video
# challenge was to finish of code from video so challenge is included in the videos code snippets section

name = input("Name: ").strip().capitalize()
Date_of_birth = input("Date of birth: ").strip()
phone_number = input("Telephone number: ").strip()
email_address = input("Email: ")
address = input("Address: ")
Contact = {"Name":name, "Date of Birth":Date_of_birth, "Telephone number":phone_number, "Email address":email_address, "Address":address}
print()
print(f"Name: {Contact["Name"]}")
print(f"Date of Birth: {Contact["Date of Birth"]}")
print(f"Telephone number: {Contact["Telephone number"]}")
print(f"Email address: {Contact["Email address"]}")
print(f"Address: {Contact["Address"]}")

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment


# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# 1 - square brackets
# 2 - fruit = ["apple","banana","pear"]
#          print(fruit[0])
# 3 - fav_dictionary = {"Fruit": apple, "Drink": water}
#             print(f"Favourite fruit: {fav_dictionary["Fruit"]}")
# 4 - list = []
#     change_list = input("Would you like to add or remove something from your list (A/R): ")
#     if change_list == "A":
#        item = input("What would you like to add?: ")
#        list.append(item)
#     elif change_list == "R":
#        item = input("What would you like to remove?: ")
#        list.remove(item)