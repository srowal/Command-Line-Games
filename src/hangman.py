import random
from words_and_drawings import words
from words_and_drawings import drawings

#game logic
def game_loop():
    word = random.choice(words).upper()
    hidden_word = "_" * len(word)
    guessed_letters = []
    num_wrong_guesses = 0
    limit = 6

    print("Welcome to HANGMAN, let's begin!")
    print_hangman(num_wrong_guesses, hidden_word)
    while hidden_word != word and num_wrong_guesses < limit:

        guess = input("Guess a letter \n=>").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed this letter, try again.")
                guessed_letters.append(guess)
            if guess not in word:
                print("Wrong guess,", guess, "is not in the word.")
                num_wrong_guesses += 1
            else:
                print("Good guess,", guess, "is in the word")
                guessed_letters.append(guess)
                for x in find(word, guess):
                    hidden_word = hidden_word[:x] + guess + hidden_word[x+1:]
        
        elif len(guess) == len(word) and guess.isalpha():
            if word == guess:
                hidden_word = word
            else:
                print("Wrong guess,", guess, "is not the correct word.")
                num_wrong_guesses += 1

        else:
            print("Invalid guess, please try again.")
        
        print_hangman(num_wrong_guesses, hidden_word)

    if hidden_word == word:
        print("Good Job, you correctly guessed", word)
    else:
        print("The word was", word, ". Better luck next time!")

def find(str, c):
    return [i for i, letter in enumerate(str) if letter == c]   

#prints current state of the hangman and word
def print_hangman(drawing_progress, word_progress):
    print(drawings[drawing_progress])
    print(word_progress, "\n\n")


if __name__ == '__main__':
    game_loop()
