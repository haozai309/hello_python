from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
	guess = int(raw_input("A number in [1, 10], your guess: "))
	if guess == random_number:
		print "You win!"
		break
	guesses_left -= 1
else:
	print "You lose."
	print "random number is %s" % (random_number)