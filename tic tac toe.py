import draw_board
import player as p
import re

#initilizing game varables
Gamestate = True
board = draw_board.initilize_board()
Turn = 0

Valid_input = False
P1 = input("Is player 1 human (H) or computer (C): ").upper()
while not Valid_input:
	if P1 == "H" or P1 == "C":
		Valid_input = True
	else:
		P1 = input("Please only enter H or C: ").upper()

Valid_input = False
P2 = input("Is player 2 human (H) or computer (C): ").upper()
while not Valid_input:
	if P2 == "H" or P2 == "C":
		Valid_input = True
	else:
		P2 = input("Please only enter H or C: ").upper()

player_dict = {
	0:P1,
	1:P2
}

print("Player 1 is",player_dict[0],"and player 2 is",player_dict[1])

draw_board.draw_board(board)
while Gamestate:
	Valid_input = False
	print("Player",Turn+1,"turn.")
	if player_dict[Turn]=="H":
		str_cordinate = input("Please enter a cell to play in. In the form int,int: ")
		while not Valid_input:
			if re.match('^[1-3],[1-3]',str_cordinate):
				x=int(str_cordinate.split(",")[0])-1
				y=int(str_cordinate.split(",")[1])-1
				if board[x][y] == None:
					board[x][y] = Turn
					Valid_input = True
				else:
					str_cordinate = input("Please chose an empty cell: ")
			else:
				str_cordinate = input("Please enter you cell in the form int,int: ")

	else:
		x,y=p.compitant_player(board,Turn)
		board[x][y]=Turn
	#check state of game
	draw_board.draw_board(board)
	state = draw_board.check_game_state(board)
	if state == "win":
		print("Player",Turn+1,"wins.")
		Gamestate = False
	elif state == "draw":
		print("Draw")
		Gamestate = False


	if Turn==1:
		Turn = 0
	else: 
		Turn = 1

	if not Gamestate:
		decided = False
		repeat = input("Do you want to play another game? (y/n) ").lower()
		while not decided:
			if repeat == "y":
				board = draw_board.initilize_board()
				Gamestate = True
				decided = True
			elif repeat == "n":
				decided = True
			else:
				repeat = input("Do you want to play another game? (y/n) ").lower()