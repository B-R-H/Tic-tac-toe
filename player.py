import random as r

def random_player(board):
	#Random player
	not_placed = True
	while not_placed: 
		x=r.randint(0,2)
		y=r.randint(0,2)
		if board[x][y]==None:
			return [x,y]

def check_line(start_cordinate,direction,board):
	line_values = []
	if direction == "v":
		#virtical code
		for i in range(3):
			line_values.append(board[start_cordinate[0]][i])
	elif direction == "h":
		#horizontal code
		for i in range(3):
			line_values.append(board[i][start_cordinate[1]])
	elif direction == "d":
		#diagnol code
		line_values = [board[start_cordinate[0]][0],board[1][1],board[2-start_cordinate[0]][2]]
	return line_values

def finishing_a_line(vls,hls,dls,player):
	for i in vls:
		if i.count(player)==2 and i.count(None) != 0:
			return [vls.index(i),i.index(None)]
	for i in hls:
		if i.count(player)==2 and i.count(None) != 0:
			return [i.index(None),hls.index(i)]
	for i in dls:
		if i.count(player)==2 and i.count(None) != 0:
			if i.index(None)==1:
				return[1,1]
			elif dls.index(i)==0:
				return [i.index(None),i.index(None)]
			else:
				return[2-i.index(None),i.index(None)]
	return [None,None]

def compitant_player(board,player):
	turn_number = 9-sum((x).count(None) for x in board)
	print("Current turn is",turn_number)
	if turn_number == 0:
		return [0,0]
	elif turn_number == 1:
		if board[0][0] == None:
			return[0,0]
		return [1,1]
	else:
		#Getting all of the values of the lines on the board
		vls=[check_line([0,0],"v",board),check_line([1,0],"v",board),check_line([2,0],"v",board)]
		hls=[check_line([0,0],"h",board),check_line([0,1],"h",board),check_line([0,2],"h",board)]
		dls=[check_line([0,0],"d",board),check_line([2,0],"d",board)]

		#wining line
		x,y = finishing_a_line(vls,hls,dls,player)
		if x!=None:
			return[x,y] 

		#blocking line
		x,y =  finishing_a_line(vls,hls,dls,(player+1)%2)
		if x!=None:
			return[x,y]
		

	x,y = random_player(board)
	return [x,y]