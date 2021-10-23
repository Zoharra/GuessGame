#Guessing Game
import random 
UserGuesses=[""]
animal_list = ["cat", "dog","shrimp","walrus"]
food_list = ["hamburger","pasta"]
Play_game = True
secret_word = ""
hint = 0
guess_input = ""
congame = False
def game() :
	while Play_game == True:
		user_input = input("Welcome to the Guessing Game." " Press a for animal list or f for food list. \n > ").lower()
		if user_input == "a":
			game.secret_word = random.choice(animal_list)
		elif user_input =="f" :
			game.secret_word = random.choice (food_list)
		else:
			print("Sorry please choose animals or food.")
			continue 
		
		break
	return
def hints() :
	yes_hint = input ("I have selected my word. Now its your turn to guess it. Press H for a hint.   \n  >  ").lower()
	num = 0
	if yes_hint == "h":
		for i in game.secret_word:
			i = num
			num += 1
		print(f"My word has {num} letters")
	else: 
		print ("You need a hint. .")
		
		
	if game.secret_word == "cat":
		print (" It starts with a c and is fluffy.")
	elif game.secret_word == "dog":
		print ("It starts with a D and is sometimes fuzzy.")
	elif game.secret_word == "shrimp":
		print ("This fish starts with a S and is part of the crab family.")
	elif game.secret_word == "walrus":
		print ("This sea animal starts with a w and barks. ")
	elif game.secret_word == "pasta":
		print ("My word starts with a P and its used a lot in american noodle dishes.")
	elif game.secret_word == "hamburger":
		print ("My words starts with H and has 2 buns and meat.")
	return
def guess() :
	 print("Now its time to guess my word. I'll go easy and give you 2 guesses. ")
	 guess.guess_input = input("> ")
	 return
def c_guess():
 	if guess.guess_input != game.secret_word :			
 		print("Nice try, but thats not it. Please look at  the hint again.")
 		guess.guess_input = input("> ")
 		
 	if guess.guess_input == game.secret_word:
 			print ("You have won!! Good Job!")
 	elif print ("wowww"):
	 		return
def loopgame():
	congame = False
	while congame == False:
		print ("Do you want to continue game? Press Y for yes or N for no.")
		yesno = input (">").lower
		if yesno != "y" .lower:
			break
		else:
			comgame = True 
			game()
			hints()
			guess()
			c_guess()
			loopgame()
	return

game ()
hints()
guess()	 
c_guess()
loopgame()