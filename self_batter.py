
from random import randint

board = []


def make_ships(board, size):
    for i in range(size):
        board.append(["O"] * size)

    for i in range(size):
    	ship_row = randint(0, size - 1)
    	ship_col = randint(0, size - 1)
    	board[ship_row][ship_col] = "B"

def print_board(board):
	for row in board:
		print " ".join(row)


make_ships(board, 8)
print_board(board)
