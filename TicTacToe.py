import os

def draw_board(board):
	os.system('cls||clear')
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))
	print('{0:^5} | {1:^5} | {2:^5}'.format(board[0], board[1], board[2]))
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))
	print('{0:<15}'.format('---------------------'))
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))
	print('{0:^5} | {1:^5} | {2:^5}'.format(board[3], board[4], board[5]))
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))
	print('{0:<15}'.format('---------------------'))
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))
	print('{0:^5} | {1:^5} | {2:^5}'.format(board[6], board[7], board[8]))
	print('{0:^5} | {1:^5} | {2:^5}'.format(' ', ' ', ' '))


	if (board[0] == board[1] == board[2] == 'X') or (board[0] == board[3] == board[6] == 'X') or (board[6] == board[7] == board[8] == 'X') or (board[2] == board[5] == board[8] == 'X') or (board[0] == board[4] == board[8] == 'X') or (board[2] == board[4] == board[6] == 'X') or (board[3] == board[4] == board[5] == 'X') or (board[1] == board[4] == board[7] == 'X'):
		print("Congratulations! X has won")
		return True
	elif (board[0] == board[1] == board[2] == 'O') or (board[0] == board[3] == board[6] == 'O') or (board[6] == board[7] == board[8] == 'O') or (board[2] == board[5] == board[8] == 'O') or (board[0] == board[4] == board[8] == 'O') or (board[2] == board[4] == board[6] == 'O') or (board[3] == board[4] == board[5] == 'O') or (board[1] == board[4] == board[7] == 'O'):
		print("Congratulations! O has won")
		return True

	return False



def start_game():

	start_ans = input('Do you want to start the game? (Yes/No): ').lower()

	if start_ans == 'yes':
		print("Let's start the game")
		play_game()
	elif start_ans == 'no':
		print(':(')
		return 'no'
	else:
		print('Answer only in yes or no')


def play_game():

	board_status = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
	draw_board(board_status)

	turn = None

	while(turn == None):

		char_choice = input('\nWhich character would you like to choose? (X/O): ')

		if char_choice == 'X' or char_choice == 'x':	
			print("It's X's turn first\n")
			turn = 1
		elif char_choice == 'O' or char_choice == 'o':
			print("It's O's turn first\n")
			turn = 0
	

	while True:
		if not(' ' in board_status):
			print("The match has been drawn")
			break
		if(turn == 1):
			x_input = int(input("\nX: Give your input (from 1-9): "))
			while x_input not in range(1,10):
				x_input = int(input("\nX: Give input in valid range only (from 1-9): "))
			while board_status[x_input-1] == 'X' or board_status[x_input-1] == 'O':
				x_input = int(input('\nThat place is already occupied. Give another input: ')) 
			board_status[x_input-1] = 'X'
			r = draw_board(board_status)
			if r == True:
				break
			turn-=1
		elif(turn == 0):
			o_input = int(input("\nO: Give your input (from 1-9): "))
			while o_input not in range(1,10):
				o_input = int(input("\nO: Give input in valid range only (from 1-9): "))
			while board_status[o_input-1] == 'X' or board_status[o_input-1] == 'O':
				o_input = int(input('\nThat place is already occupied. Give another input: '))
			board_status[o_input-1] = 'O'
			r = draw_board(board_status)
			if r == True:
				break
			turn+=1


def init():
	choice = start_game()
	if not(choice == 'no'):
		while(input('\nDo you want to restart the game? (yes/no): ').lower() == 'yes'):
			play_game()

init()
