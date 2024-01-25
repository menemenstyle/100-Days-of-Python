print("""                          _ ___ _  _ _   _
                    |\  /||(_  | |_)|_(_  (_
                    | \/ ||__) | | \|___) __)
                    __    _   _ ___      _, _
                   /  |_||_)|(_  | ||\ |(_ (_
                   \__| || \|__) | || \|(_ __)
                   ||    Adult toy shop     ||
   ________________||_______________________||_____________
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_||
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|| /|
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_||/||
  |_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|||/|
  |_|_|_|_|_|_|_|_|_|     _      _     |_|_|_|_|_|_|_|_|_|_|/||
  |_| books  movies |    (_)    (_)    |latex __  leather|_|/||
  |_|.    smut      |__________________|     (^^)  .     |_||/|
  |_|*`.            |_|      ||      |_|     _)(_  I`.   |_|/||
  |_| S `.          |_| llup || push |_|    /()()\/| ;   |_||/|
  |_|`. A `.        |_| tuo  ||  in  |_|   // )_\\/      |_|/||
  |_|  `. L `.      |_|     [||]     |_|   \|.//_)       |_||/|
  |_|    `. E `.    |_|      ||      |_|     // /        |_|/||
  |_|______`__*_`___|_|      ||      |_|_____\\|_________|_||/|
  |_|_|_|_|_|_|_|_|_|_|______||______|_|_|_|_|_|_|_|_|_|_|_|/||
__|_|_|_|_|_|_|_|_|_|_|______||______|_|_|_|_|_|_|_|_|_|_|_||/________
 /     /     /     /     /     /     /     /     /     /     /     /
/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/
__________________________________________________________________
 /_/_/_/
""")

print("Welcome to the Treause Island.\nYour mission is to find the treasure.")
direction = input("You need to move. Type 'left' or 'right'.\n")
dir = direction.lower()
if dir == "left":
    movement = input("You come at a lake. There is a island in the middle. Do you want to 'swim' or 'wait' for a boat?\n")
    move = movement.lower()
    if move == "wait":
        doors = input("You come to the island. There are three doors. One is 'blue', one is 'red', and the other one is 'yellow'. Which one?\n")
        door = doors.lower()
        if door == "yellow":
            print("CONGRATULATIONS! YOU WIN!")
        elif door == "red":
            print("Oh no! There was wild fire inside. You burned alive. GAME OVER.")
        elif door == "blue":
            print("Oh no! You got eaten by hungry wolves. GAME OVER.")
        else:
            print("Oh no! You died due to indecisiveness. GAME OVER.")
    else:
        print("Oh no! You got attacked by a shark. GAME OVER.")
else:
    print("Oh no! You feel into a hole. GAME OVER.")
