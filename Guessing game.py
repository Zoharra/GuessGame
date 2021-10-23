import random
import time

animal_list = ["cat", "dog", "shrimp", "walrus"]
food_list = ["hamburger", "pasta"]
secret_word = ''
hint = 0
num = 0
GuessTrials = 5
UserScore = 0
Round = 1
# Created dictionary using possible secret words as keys and corresponding hints as value .
HINTS = {"cat": "It starts with a c, lands on its paws and is fluffy", "dog": "It starts with a D , dislikes water and is sometimes fuzzy.",
         "shrimp": "The fish stats with a S and is a crustacean ", "walrus": "It starts with a w, has tusks and barks.",
         "hamburger": "my word stats with a H, has two buns and a meat", "pasta": "my word starts with a P and its used "
                                                                                  "a lot in American noddle dishes,"}

# DEFINING FUNCTIONS:

def choose_category():
    global secret_word
    while True :
        user_input = input(" Enter A for an animal list or F for a food list. :").lower()
        if user_input == "a":
            secret_word = random.choice(animal_list)
        elif user_input == "f":
            secret_word = random.choice(food_list)
        else :
            print("Sorry please choose animals or food by entering either A or B ")
            continue
        return secret_word

def hints():
    global num
    print("I have selected my word; here is a clue.")
    # Transversing the keys of HINTS and printing the corresponding hint for the secret word.
    for i in HINTS:
        if i == secret_word:
            print(HINTS[i])
    nom = len(secret_word) # used the len function to give the length of the secret word
    num = nom
    yes_hint = input("Enter H for a hint. :").lower()
    if yes_hint == 'h':
        print(f"My word has {num}letters")
    else:
        print("You might need a hint...")

def take_guess():
    if GuessTrials == 5:
        print("I'll go easy on you this round and give you 5 guesses")
    else:
        print(f"You have {GuessTrials} guesses")
    time.sleep(0.2)
    take_guess.guess_input = input("Now it's time to guess my word\nTake a guess\n:").lower()


def check_guess():
    global UserScore
    global num
    trial = 0
    while True:
        if take_guess.guess_input != secret_word:
            print("Nice try, but that's not it.")
            if trial == GuessTrials:
                print("You have exhausted your guesses")
                UserScore += 0
                print("You didn't win any mark this round.")
                break
            take_guess.guess_input  = input("Take a guess.\n:")
            trial += 1
            if trial == 1:
                print(f"My word has {num}letters")
                continue
        elif take_guess.guess_input == secret_word:
            print("CORRECT!!!!")
            time.sleep(0.2)
            print("You have won 10 marks\n GOOD JOB!")
            UserScore += 10
            if trial < 1:
                UserScore +=2
                print("You have gotten 2 extra marks as you guessed correctly on your first trail.")
            break

def update():
    global Round
    global GuessTrials
    Round += 1
    if GuessTrials > 2 :
        GuessTrials -=1 # To reduce the number of guess each round till it gets to 2 guesses.

give_score = f"You scored{UserScore} marks"
# Added function run_game.
def run_game():
    global Round
    while True:
        print(f"ROUND{Round}")
        choose_category()
        hints()
        take_guess()
        check_guess()
        update()
        print("Do you want to continue the game?")
        yesno = input("Enter Y to continue or N to exit game :").lower()
        if yesno != "y":
            print(f"Your total score is {UserScore}marks")
            break
        else:
            time.sleep(0.8)
            print("Here we go!")
            run_game()

# Starting program
print("Welcome to the Guessing game!")
time.sleep(0.5)
run_game()

