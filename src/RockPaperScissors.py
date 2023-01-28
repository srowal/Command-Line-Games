import random;

def gameLoop():
    while True:
        player = input("\nEnter 'r' for rock, 'p' for paper, 's' for scissors\n->")

        rps = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        comp = random.choice(['rock', 'paper', 'scissors'])

        try:
            print("You picked", rps[player])
            print("Computer picked", comp)

            if rps[player] == comp:
                print("Its a tie.")
            elif rps[player] == 'rock' and comp == 'scissors' or rps[player] == 'paper' and comp == 'scissors' or rps[player] == 'scissors' and comp == 'paper':
                print("Player wins");
            else:
                print("Computer wins")

            restart = input("\nPlay Again? (y/n)\n->")
            if restart == 'y':
                continue
            elif restart =='n':
                break
            else :
                print("incorect input, terminating")
                break;
        except KeyError:
            print("Incorrect input, please try again.")

    print("Thanks for playing.")
    
if __name__=="__main__":
    gameLoop()