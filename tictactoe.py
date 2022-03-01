#TIC-TAC-TOE

board = {
    '1':' ', '2': ' ', '3':' ', '4': ' ', '5':' ', '6': ' ', '7':' ', '8': ' ', '9':' '
}
 
def printBoard(gameBoard):
    print("{}|{}|{}".format(gameBoard['1'],gameBoard['2'],gameBoard['3']))
    print("-+-+-")
    print("{}|{}|{}".format(gameBoard['4'],gameBoard['5'],gameBoard['6']))
    print("-+-+-")
    print("{}|{}|{}".format(gameBoard['7'],gameBoard['8'],gameBoard['9']))
    #print("-+-+-")
    
def game():
    gameBoard = board
    turn = 'X'
    count = 0
    print()
    for i in range(1000):
        print("Game board:{}".format(printBoard(gameBoard)))
        print("It is {}'s turn".format(turn))
        validPos = True
        while validPos:
            n = input("Enter the box number:")
            if gameBoard[n] != ' ':
                print("Aldready filled")
            else:
                validPos = False
        gameBoard[n] = turn
        count += 1
        
        win = False
        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                win = True
            if gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                win = True
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                win = True
            if gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                win = True
            if gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                win = True
            if gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                win = True
            if gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                win = True
            if gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
                win = True
        if win == True:
            print("{} won".format(turn))
            return
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
        if count == 9:
            print("TIE")
            return
        
game()
