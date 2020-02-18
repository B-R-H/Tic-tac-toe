def initilize_board():
	return [[None,None,None],[None,None,None],[None,None,None]]

def draw_board(board):
	print("_________") 
	for j in range(3):
		string = ""
		for i in range (3):
			if board[i][j]==0:
				string += "|O|"
			elif board[i][j]==1:
				string += "|X|"
			else:
				string += "| |"
		print(string)
		print("_________")

def check_game_state(board):
	
	#diagnols
	if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0] != None:
		print("diagonal win")
		return "win"
	if board[2][0]==board[1][1] and board[2][0]==board[0][2] and board[1][1] != None:
		print("diagonal win")
		return "win"

	#verticals
	for i in range(3):
		row_win = True
		wining_line=[]
		for j in range(3):
			if j == 0:
				wining_line.append([j,i])
				test_val_h = board[j][i]
				if test_val_h == None:
					row_win = False
					break
			elif board[j][i] != test_val_h:
				wining_line.append([i,j])
				row_win = False
				break
		if row_win:
			print("Horizontal win")
			return "win"

	#horizontals
	full_board = True
	for i in range(3):
		row_win = True
		wining_line=[]
		for j in range(3):
			wining_line.append([i,j])
			if board[i][j]==None:
				full_board = False
			if j == 0:
				test_val_h = board[i][j]
				if test_val_h == None:
					row_win = False
					break
			elif board[i][j] != test_val_h:
				row_win = False
		if row_win:
			print("Vertical win")
			print(wining_line)
			return "win"
	if full_board:
		return "draw"

	return "starnd play" 