def Board():
    numrows = 3
    
    #Generate 2d-grid-array with empty space as placeholder for elements
    board = [['   '] * (numrows + 2) for x in range(numrows + 2)]
    
    #Add borders to the odd numbered rows and columns
    for row in range(numrows + 2):
        for col in range(numrows + 2):
            if row %  2 == 1:
                board[row][col] = '___'
            if col % 2 == 1:
                board[row][col] = '|'
    
    #Add last set of column borders in the last row 
    board.append(['   '] * (numrows + 2))
    board[numrows + 2][1] = '|'
    board[numrows + 2][3] = '|'
    

    for row in board:
        print(''.join(row))
    return board
    
    




def getMovesMap(board): 
    '''Build dictionary mapping single digit user input to board position; return
    movesmap so that we can use dictionary to map user input for moves'''
    
    movesmap = {}
    i = 0
    for row in range(0, len(board), 2):
        movesmap[row + (i + 1)] = [row, 0]
        movesmap[row + 2 + i] = [row, 2]
        movesmap[row + 4 + (i - 1)] = [row, 4]
        i += 1
    
    return movesmap



def playTicTacToe():
   
    
    #Start of the game, printing empty board and instructions
    print("\n\nLet's play Tic-Tac-Toe!\n")
    board = Board()
    movesmap = getMovesMap(board)
    
    #Player 1 is X and player 2 is O
    print('\nPlayer 1 plays piece X. Player 2 plays piece O.')
    p1piece = ' X '
    p2piece = ' O '
    
   


playTicTacToe()