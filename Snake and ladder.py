import random

# function to play the game
def play_game():
    print("Let's play Snake and Ladder Game!")
    pos = 0
    # dice roll
    while True:
        roll = random.randint(1, 6)
        print("Roll the dice:", roll)
        # options to move up or down
        options = input("Press 1 to climb the ladder\nPress 2 to go down the snake\n")
        if options == '1':
            pos += roll
        elif options == '2':
            pos -= roll
        # check for win/loss
        if pos < 0:
            print("You lost! Better luck next time.")
            break
        elif pos > 10:
            pos = 10
        print("Move to position:", pos)
        # check for win
        if pos == 10:
            print("You won! Congratulations.")
            break

play_game()