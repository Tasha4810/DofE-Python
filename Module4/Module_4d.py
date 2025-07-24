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


