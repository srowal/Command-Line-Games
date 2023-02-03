import random

#game logic
def gameLoop():
    
    gameState = [1,2,3,4,5,6,7,8,9]
    turn = random.choice(['X', 'O'])
    print("Welcome to Tic-tac-toe!")
    printTable(gameState)

    while not checkForWin(gameState, turn) and not checkForTie(gameState):
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        print(turn,"turn\n")
        promptInput(gameState, turn)
        printTable(gameState)

    print("\n\nThanks for playing!");

#prints the current state of the game
def printTable(t):

    print("\n\n {} | {} | {} ".format(t[0], t[1], t[2]))
    print("-----------")
    print(" {} | {} | {} ".format(t[3], t[4], t[5]))
    print("-----------")
    print(" {} | {} | {} \n\n".format(t[6], t[7], t[8]))

#returns true and prints message if a player has won
def checkForWin(t, x_or_o):
    win = False

    for x in range(0,8,3):
        if t[x] == t[x+1] and t[x] == t[x+2]:
            win = True

    for x in range(0,2):
        if t[x] == t[x+3] and t[x] == t[x+6]:
            win = True

    if t[0] == t[4] and t[0] == t[8] or t[2] == t[4] and t[2] == t[6]:
        win = True

    if win:
        print("{} wins".format(x_or_o))

    return win

#returns true and prints message if a players have tied
def checkForTie(t):
    tie = True
    for x in range(0,8):
        if t[x] != 'X' and t[x] != 'O':
            tie = False
    if tie:
        print("It's a TIE.")
    return tie        

#promts the user for an input and validates saif input
def promptInput(t, x_or_o):
    while True:
        pos = input("Please select position.\n=>")
        try:
            pos = int(pos) - 1
            if pos > 8 or pos < 0:
                print("ERROR, invalid selection.")
            elif t[pos] == 'X' or t[pos] == 'O':
                print("This position is taken please pick another.")
            else:
                t[pos] = x_or_o
                break
        except ValueError:
            print("ERROR, input is not a valid integer.")
        


if __name__ == "__main__":
    gameLoop()