
import random;

def gameLoop():
    num = random.randint(1, 100)
    print('Guess an integer between 1 and 100');

    while True:
        try: 
            guess = input('->')
            guess = int(guess)
            
            if guess > 100 or guess < 1:
                print("ERROR integer out of bounds,")
            elif guess == num:
                print("CORRECT the number is ", num)
                break
            elif guess < num:
                print("A bit higher,")
            else :
                print("A bit lower,")
            
        except ValueError:
            print("This is not an integer,")
            
        print("Try again.")

if __name__ == "__main__":
    gameLoop()