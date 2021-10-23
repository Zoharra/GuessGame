#Guessing Game
# Substituted press with enter
# Removed the variable play_game.
import random
import time

UserGuesses = []
animal_list = ["cat", "dog", "shrimp", "walrus"]
food_list = ["hamburger", "pasta"]
secret_word = ''
hint = 0
num = 0
UserScore = 0
#Added a dictionary using animals as keys and corresponding hints as value .
HINTS = {"cat": "It starts with a c and is fluffy", "dog": "It starts with a D and is sometimes fuzzy.",\
         "shrimp": "The fish stats with a S and has a tail", "walrus": "It starts a w and has tusks.",\
         "hamburger": "like a sandwich", "pasta": "noddles"}

print("Welcome to the Guessing game!")
# Renamed the function game to choose_category
def choose_category():
    global secret_word
    while True :
        user_input = input(" Enter 'a' for an animal list or 'f' for a food list. :").lower()
        if user_input == "a":
            secret_word = random.choice(animal_list)
        elif user_input == "f":
            secret_word = random.choice(food_list)
        else :
            print("Sorry please choose animals or food")
            continue
        return secret_word

# Modified the hints function.
def hints():
    print("I have selected my word. Now it's your turn to guess it.")
    print("Here is a clue")
    for i in HINTS:
        if i == secret_word:
            print(HINTS[i])
    yes_hint = input("Enter H for a hint. :").lower()
    if yes_hint == 'h':
        num = len(secret_word)
        # used the len function to give the length of the secret word
        print(f"My word has {num}letters")
    else:
        print("You might need a hint...")

    # Transversing the keys of HINTS and printing the corresponding hint for the secret word.


def take_guess():
    print("Now it's time to guess my word\n I'll go easy on you and give you two guesses")
    take_guess.guess_input = input("Take a guess.\n:")
    # Added the input prompt for a more convenient interface.

# Renamed function from c_guess to check guess.
def check_guess():
    while True:
        if take_guess.guess_input != secret_word:
            print("Nice try, but that's not it.\n kindly take a look at the hint")
            hints()
            # Called the int function to display the hint again
            continue
        elif take_guess.guess_input == secret_word:
            print("CORRECT!!!!")
            print("You have won 10 marks\n GOOD JOB!")
            global UserScore
            UserScore += 10
            break

# Added function run_game.
def run_game():
    choose_category()
    hints()
    take_guess()
    check_guess()
    while True:
        print("Do you want to continue the game?")
        yesno = input("Enter Y to continue or N to exit game.").lower()
        if yesno != "y":
            print(f"Your total scorce is {UserScore}")
        else:
            run_game()
    # Modified previous function into run_game.

run_game()

