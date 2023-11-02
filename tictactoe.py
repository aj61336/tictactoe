def main():
    # Print the header information for the game
    print("Tic Tac Toe")
    print("Goal: Get three of your character (X or O) in a row")
    print("Rules")

# Create gameboard using a list board=[["1","2","X"], ["4","X","6"], ["X","8","9"]]    
board=[["1","2","X"], ["4","X","6"], ["X","8","9"]]

def printBoard(board):
    # Print the board using a list
    print(" "+board[0][0]+" |"+" "+board[0][1]+" |"+" "+board[0][2]+" ")
    print("-----------")
    print(" "+board[1][0]+" |"+" "+board[1][1]+" |"+" "+board[1][2]+" ")
    print("-----------")
    print(" "+board[2][0]+" |"+" "+board[2][1]+" |"+" "+board[2][2]+" ")

def inputValidation(rowOrCol):
    value=int(input("Enter the "+rowOrCol+" number: "))-1 # array index is 1 less than user value
    
    # validate row input
    while(value>2 or value<0):
        value=int(input("ERROR! Enter the "+rowOrCol+" number: "))-1 # array index is 1 less than user value

    return value

def isSpaceAvailable(board, row, col):
    

def checkWin():
        # Create variable for winning player
    winner="NONE"

    # Check for a win
    if(board[0][0]==player and board[0][1]==player and board[0][2]== player): # 1st row
        winner=player
    elif(board[1][0]==player and board[1][1]==player and board[1][2]== player): # 2nd row
        winner=player
    elif(board[2][0] == player and board[2][1] == player and board[2][2] == player): # 3rd row
        winner=player
    elif(board[0][0] == player and board[1][0] == player and board[2][0] == player): # 1st col
        winner=player
    elif(board[0][1] == player and board[1][1] == player and board[2][1] == player): # 2nd col
        winner=player
    elif(board[0][2] == player and board[1][2] == player and board[2][2] == player): # 3rd col
        winner=player
    elif(board[0][0] == player and board[1][1] == player and board[2][2] == player): # \ diagonal
        winner=player
    elif(board[2][0] == player and board[1][1] == player and board[0][2] == player): # / diagonal
        winner=player
        
    print(player+" Wins")
def changeTurn(player):
    if(player==X):
        player=O
    else:
        player=X
    return player
# change players turn

printBoard(board)
X="X"
O="O"
player=X

    

    # Loop for choosing an acceptable square
    ## 123
    ## 1 ABC
    ## 2 DEF
    ## 3 GHI




playAgain=True

while(playAgain):
        # play game
        
        # Ask to play again
    answer=input("Would you like to play again (y/n)?")
## if(answer.lower()=="y"):
## playAgain=True
    if(answer.lower()=="n"):
        playAgain=False
if(__name__=="__main__"):
    main()
