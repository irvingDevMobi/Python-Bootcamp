CAT_SIZE = 3
P1_NAME = "Jessica"
P2_NAME = "Irving"
P1_SYMBOL = 'X'
P2_SYMBOL = 'O'
EMPTY_SYMBOL = ' '
EXIT = 'q'

logicBoard = [[]]
isWinner = False
isFirstPlayer = True;

def intro():
	print("\n### Tic Tac Toe ###\n");
	print("Intructions: Play with another friend")
	print("Type the ROW number then space and finally COLUMN number\n") 

def newGame():
	global logicBoard
	global isWinner
	
	isWinner = False
	logicBoard = [[EMPTY_SYMBOL for c in range(CAT_SIZE)] for r in range(CAT_SIZE)]
	
	
def printBoard():
	print()
	for r in range(len(logicBoard)):
		for c in range(len(logicBoard[r])):
			endLine = " | "
			if c == len(logicBoard[r]) - 1:
				endLine = "\n"
			print(logicBoard[r][c], end = endLine)	
		if r < len(logicBoard) - 1:
			print("__________")
	print()

def readInputValue(userName):
	cells = input(userName + " Next Movement: ").split(" ");
	if len(cells) == 2 and cells[0].isdecimal() and cells[1].isdigit():
		row = int(cells[0])
		col = int(cells[1])
		if isValidCell(row, col):
			return [row - 1, col - 1]
	print("Bad Input Try again, Type the row number then space and finally column number\n example=> '1 3'\n")	
	return readInputValue(userName)
	
def isValidCell(row, col):
	return row > 0 and row <= CAT_SIZE and col > 0 and col <= CAT_SIZE and logicBoard[row - 1][col - 1] == EMPTY_SYMBOL

def savedInput(row, col, isFirstPlayer):
	global logicBoard
	symbol = P1_SYMBOL if isFirstPlayer else P2_SYMBOL
	logicBoard[row][col] = symbol

def playerWin(isFirstPlayer):
	symbol = P1_SYMBOL if isFirstPlayer else P2_SYMBOL
	isWinner = False
	faultDiagonal = False
	faultReverseDiagonal = False
	for r in range(CAT_SIZE):
		faultHorizontal = False
		faultVertical = False
		for c in range(CAT_SIZE):
			if not faultHorizontal and symbol != logicBoard[r][c]:
				faultHorizontal = True
			if not faultVertical and symbol != logicBoard[c][r]:
				faultVertical = True
			if faultHorizontal and faultVertical:
				break
		if not faultHorizontal or not faultVertical:
			return True
		if not faultDiagonal and symbol != logicBoard[r][r]:
			faultDiagonal = True
		if not faultReverseDiagonal and symbol != logicBoard[-r - 1][r]:
			faultReverseDiagonal = True
	if not faultDiagonal or not faultReverseDiagonal:
		return True
	return False			
		
def game():
	global isWinner
	global isFirstPlayer
	
	TOTAL_TURNS = CAT_SIZE * CAT_SIZE
	
	intro()
	newGame()
	turnCounter = 0;
	
	while(not isWinner and turnCounter < TOTAL_TURNS):
		printBoard()
		playerName = P1_NAME if isFirstPlayer else P2_NAME
		cells = readInputValue(playerName)
		savedInput(cells[0], cells[1], isFirstPlayer)
		if playerWin(isFirstPlayer):
			printBoard()
			print(playerName + " is the Winwer!!!!")
			isWinner = True
		isFirstPlayer = not isFirstPlayer
		turnCounter += 1
	if not isWinner:
		print("\nthere was a Tie") 

def restart():
	keyInput = input("\nType 'q' to exit the game or another key to play again: ")
	if keyInput != EXIT:
		gameLoop()
	
def gameLoop():
	game()
	restart()

gameLoop()