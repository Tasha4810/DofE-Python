# ===============================================================
# Video Follow Along: Day 17 - continue statement
# ===============================================================
# This contains code snippets I create as I follow the video

while True:
    print("you are in a corridor, do you go left or right ")
    direction = input("> ")
    if direction == "left":
        print("you have fallen to your death")
        break
    elif direction == "right":
        continue
    else:
        print("Ahh! you're a genius, you've won")
        print("just kidding try again bozo")
        exit()
print("The game is over, you've failed!")

# ===============================================================
# Video Day 17 Challenge: continue statement
# ===============================================================
# This contains the code I created for the challenged posed in the video

print("M O R E   E P I C   'R O C K  P A P E R  S C I S S O R S' B A T T L E  ")
counter = 1

print()
while True:
    print(f"Round {counter} ")
    print()
    print("select your move (R, P or S)")
    print()
    player_1_move = input("Player 1 > ")
    Player_2_move = input("Player 2 > ")
    if player_1_move == "S" and Player_2_move == "P":
        print("Player2's paper has been sliced by Player1's scissors!")
        print("Player 1 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif player_1_move == "P" and Player_2_move == "R":
        print("Player2's rock has been smothered by Player1's paper!")
        print("Player 1 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif player_1_move == "R" and Player_2_move == "S":
        print("player2's scissors have been crushed by Player1's rock !")
        print("Player 1 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif Player_2_move == "S" and player_1_move == "P":
        print("Player1's paper has been sliced by Player2's scissors!")
        print("Player 2 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif Player_2_move == "P" and player_1_move == "R":
        print("Player1's rock has been smothered by Player2's paper!")
        print("Player 2 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif Player_2_move == "R" and player_1_move == "S":
        print("player1's scissors have been crushed by Player2's rock !")
        print("Player 2 wins!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif player_1_move == "S" and Player_2_move == "S":
        print("Player2's scissors and Player1's scissors! have clashed!")
        print("It's a tie!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif player_1_move == "R" and Player_2_move == "R":
        print("Player2's rock and Player1's rock have smashed each other!")
        print("It's a tie!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
    elif player_1_move == "P" and Player_2_move == "P":
        print("player2's paper and Player1's paper have combined to become a paper ball !")
        print("It's a tie!")
        stop_playing = input("Do you want to stop playing?: ")
        if stop_playing == "yes" or exit == "Yes":
            break
        else:
            counter += 1
            continue
print("Hope you have enjoyed the games ")

# ===============================================================
# Programs
# ===============================================================
# These are programs I create for assessment

# no program

# ===============================================================
# Quiz Module XXX: This contains the answers to my end of module quiz
# ===============================================================

# --- James ---
# Okay things are getting pretty spicy now!
# That's a mammoth of a function up there, did you type out all the options yourself?
# It has however made me angry as it is so complicated and long!
# Here's me soothing myself by making it even more complicated but shorter

# Creating a dictionary of what different combinations win. The keys here are two inputs, the value is the index of the move that wins.
# Doing is that way you don't have to write RS and SR, as they're opposites.
outcomes = {
    "RS": 0,
    "RP": 1,
    "RR": None,
    "PS": 1,
    "PP": None,
    "SS": None
}
names = {
    "R": "Rock",
    "S": "Scissors",
    "P": "Paper"
}


def quick_RPS_check(player_number):
    valid_input = False
    while not valid_input:
        print(f"Player {player_number}, select a move (R, P or S)")
        choice  = input()
        if choice.upper() in ["R", "P", "S"]:
            valid_input = True
        else:
            print("Invalid input, please re-enter (valid inputs are R, P or S)")
    return choice

# Start the game
print("\nJames has written a game of rock, paper, scissors between two players.")
print("Player 1 and Player 2 will each select a move in turn (don't let each other see)")
p1 = quick_RPS_check(1)
p2 = quick_RPS_check(2)
print(f"Player 1 played {names[p1]} and Player 2 played {names[p2]}")
winner = outcomes[p1+p2]
plays = [names[p1], names[p2]]
print(f"Player {winner+1} wins because {plays[winner]} beats {plays[not winner]}")
# That last plays[not winner] line is a cheeky one!