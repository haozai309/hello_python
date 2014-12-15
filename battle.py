
# Welcome to Battleship
# http://www.codecademy.com/courses/python-beginner-en-4XuFm/0/1?curriculum_id=4f89dab3d788890003000096

""" In this project you will build a simplified, one-player version of the 
classic board game Battleship! In this version of the game, there will be a 
single ship hidden in a random location on a 5x5 grid. The player will have 10 
guesses to try to sink the ship. """

from random import randint

board = []

for i in range(5):
    board.append(["O"]*5)
    
def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
	return randint(0, len(board) - 1)

def random_col(board):
	return randint(0, len(board) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


def check_guess(row, col, turn):
	guess_row = int(raw_input("Guess Row: "))
	guess_col = int(raw_input("Guess Col: "))

	if guess_row == ship_row and guess_col == ship_col:
		print "Congratulations! You sank my battleship"
		return True
	else:
		print "You missed my battleship!"
		if guess_row not in range(5) or \
		    guess_col not in range(5):
			print "Oops, that's not even in the ocean."
		elif board[guess_row][guess_col] == "X":
			print "You guessed that one already."
		else:
			if guess_row in range(5) and guess_col in range(5):
				board[guess_row][guess_col] = "X"
		if turn == 3:
			print "Game Over"
		return False

for turn in range(4):
	print
	print "%s" % (turn + 1)
	if check_guess(ship_row, ship_col, turn):
		break

print "Battle ship is in row %s, col %s" % (ship_row, ship_col)




