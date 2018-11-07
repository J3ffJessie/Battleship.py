from random import randint



board = []

board_count = 10 #easy way to size the board quickly

for i in range(0, board_count):

	board.append(["0"] * board_count)



def print_board(board):

	for row in board:

		print(" ".join(row))



print_board(board)		



def random_row(board):

	return randint(0, len(board) - 1)



def random_col(board):

	return randint(0, len(board) - 1)



ship_row = random_row(board)

ship_col = random_col(board)

print(ship_row)

print(ship_col)



for turn in range(4):

	print("Turn", turn + 1)

	guess_row = int(input("Guess Row:"))

	guess_col = int(input("Guess Col:"))



	if guess_row == ship_row and guess_col == ship_col:

		print("Congrats!")

		break

	else:

		if guess_row and guess_col > board_count:

			print("Not on the board")

		elif board[guess_row][guess_col] == "X":

			print("Already Guessed") 

		else:

			print("You missed!")

			board[guess_row][guess_col] = "X"

		if (turn == 3):

			print("Game Over")

		print_board(board)
