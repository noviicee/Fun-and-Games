#Guessing Game

import random

name=input("Enter your name: ")
print("Hello {}! Welcome to the Guessing Game.".format(name))
list_of_words=["appointment","bananaloveroverhere","guessing","language","sunset","macbook","caramel","canavas"]

# get a random word from this list
index=random.randint(0,len(list_of_words))
word=list_of_words[index]

#
indices=random.sample(range(0,len(word)),3)
guesses="" #characters that the user has guessed so far
for i in indices:
	guesses+=word[i]
chances=10
play="Yes"

def playagain():
	global play
	play=input("Do you want to play again?? [Yes/No]: ")
	if play=="Yes":
		global chances, word, guesses
		chances=10
		indices=random.sample(range(0,len(word)),3)
		guesses="" #characters that the user has guessed so far
		for i in indices:
			guesses+=word[i]

#play is global variable
while play=="Yes":
	while chances >0:
		won=True
		for ch in word:
			if ch in guesses: # the person has guesses this characyer correctly
				print(ch,end=' ')
			else:
				print('_',end=' ')
				won=False

		if won:
			print("\n\nCONGRATULATIONS!\nYou Won!")
			print("Your final score is:",chances*10)
			#ask if you want to play again
			playagain()
			break

		# take a guess from the player
		guess=input("Guess a character: ")
		guesses+=guess

		if guess not in word:
			chances-=1
			if chances >1:
				print("\n\nWrong Answer!\nYou have {} chances left.".format(chances))
			elif chances==1:
				print("\n\nWrong Answer!\nYou just have 1 chance left.")

			if chances==0:
				print("GAME OVER!\nYou Lose!")
				#ask if you want to play again
				playagain()
				break
print("Hope you enjoyed the game!")