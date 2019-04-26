from array import *

def printTicTac(Tic, size):
	for x in range(0, size):
		oneRow = ''
		for y in range(0, len(Tic)):
			oneRow += Tic[x][y] + ' '
		print oneRow

def checkEndGame(Tic, size):
	#Check horizontal win
	for x in range(0, size):
		win = True
		char = Tic[x][0]
		if char != '.':
			for y in range(1, size):
				if Tic[x][y] != char: #Got a win
					win = False
		else:
			win =  False
		if win == True:
			print 'Horizontal win'
			return win

	#Check vertical win
	for x in range(0, size):
		win = True
		char = Tic[0][x]	
		if char != '.':
			for y in range(1, size):
				if Tic[y][x] != char:
					win = False
		else:
			win =  False
		if win == True:
			print "Vertical Win"
			return win

	#Check diagonal win
	win = True
	char = Tic[0][0]
	if char != '.':
		for x in range(1, size):
			if Tic[x][x] != char:
				win = False
				break
	else:
		win =  False
	if win == True:
		print "Diagonal"
		return win

	#Check reverse diagonal win
	win = True
	char = Tic[0][size-1]
	if char != '.':
		for x in range(size-2, 0, -1):
			if Tic[size - 1 - x][x] != char:
				win = False
				break
	else:
		win = False
	if win == True:
		print "Rev Diag"
		return win

	return False

if __name__ == "__main__":
	size = 3
	Tic = []
	for x in range(0,size):
		Tac = []
		for y in range(0,size):
			Tac.append('.')
		Tic.append(Tac)
	endGame = False
	numPlaysLeft = size * size
	print 'TicTacToe! First player is O.'
	playerO = True
	while endGame == False and numPlaysLeft > 0:
		coordinates = raw_input('Enter coordinates of your move (y x)').split()
		try: 
			# if len(coordinates) > 2:
			# 	raise Exception
			x = int(coordinates[0])
			y = int(coordinates[1])
			if x > size-1 or y > size-1:
				raise Exception
		except:
			print 'Please enter numbers in the correct range'
			continue
		if Tic[x][y] == '.':
			if playerO == True:
				Tic[x][y] = 'O'
				playerO = False
				numPlaysLeft -= 1
			else:
				Tic[x][y] = 'X'
				playerO = True
				numPlaysLeft -= 1
			endGame = checkEndGame(Tic, size)
		else:
			print "That spot is full"
		printTicTac(Tic, size)
	print 'GAME OVER'





