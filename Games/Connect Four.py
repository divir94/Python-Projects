"""Connect Four is a variation of tic-tac-toe played on a 7x6 rectangular board.
The game is played by two players, alternating turns, with each trying to
place four checkers in a row vertically, horizontally, or diagonally.
One constraint in the game is that because the board stands vertically,
the checkers cannot be placed into an arbitrary position. A checker may only
be placed at the top of one of the currently existing columns (or it may
start a new column)."""

class Board:
    """ a datatype representing a C4 board
    with an arbitrary number of rows and cols
    """
         
    def __init__( self, width, height ):
        """ the constructor for objects of type Board """
        self.width = width
        self.height = height
        self.data = [] # this will be the board
         
        for row in range( height ):
            boardRow = []
            for col in range( width ):
                boardRow += [' '] # add a space to this row
            self.data += [boardRow] # add this row to the board
         
        # do not need to return inside a constructor!
         
         
    def __repr__(self):
        """ this method returns a string representation
        for an object of type Board
        """
        s = '\n'   # the string to return
        for row in range( self.height ):
            s += '|' # add the spacer character
            for col in range( self.width ):
                s += self.data[row][col] + '|'
            s += ' ' + str(row) + '\n'
                 
        # add the bottom of the board
        for i in range( self.width ):
            s += '--'
        s += '-\n'
        # and the numbers underneath here
        for col in range( self.width ):
            s += ' ' + str(col%10)
        s += '\n'
        return s # the board is complete, return it

    def addMove(self, col, ox):
        row = -1
        while(self.data[row][col] != ' '):
            row -= 1
        self.data[row][col] = ox

    def clear(self):
        self.data = [[' ' for col in range( self.width )] for row in range( self.height )]

    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
         
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
         
        moveString must be a string of integers
        """
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def allowsMove(self, c):
        return (0<=c<self.width and self.data[0][c] ==' ')

    def isFull(self):
        for col in range(self.width):
            if (self.allowsMove(col)): return False
        return True

    def delMove(self, c):
        row = 0
        while (row<self.height and self.data[row][c] == ' '):
            row += 1
        if (row >= self.height): return
        self.data[row][c] = ' '
        return

    def winsFor(self, ox):
        # check for horizontal wins
        for row in range(0,self.height):
            for col in range(0,self.width-3):
                if self.data[row][col] == ox and \
                self.data[row][col+1] == ox and \
                self.data[row][col+2] == ox and \
                self.data[row][col+3] == ox:
                    return True

        # check for vertical wins
        for row in range(0,self.height-3):
            for col in range(0,self.width):
                if self.data[row][col] == ox and \
                self.data[row+1][col] == ox and \
                self.data[row+2][col] == ox and \
                self.data[row+3][col] == ox:
                    return True

        # check for diagnal wins
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.data[row][col] == ox and \
                self.data[row+1][col+1] == ox and \
                self.data[row+2][col+2] == ox and \
                self.data[row+3][col+3] == ox:
                    return True
 

        # check for inverse-diagnal wins
        for row in range(self.height-3):
            for col in range(3,self.width):
                if self.data[row][col] == ox and \
                self.data[row+1][col-1] == ox and \
                self.data[row+2][col-2] == ox and \
                self.data[row+3][col-3] == ox:
                    return True
                
        return False

    def hostGame(self):
        print "Welcome to Connect Four!\n", self
        players = ['X', 'O']
        i=0
        player = players[i]
        while not(self.winsFor('X') or self.winsFor('O') or self.isFull()):
            col = int(input(player + "'s choice: "))
            while (not self.allowsMove(col)):
                print "Sorry, move is not valid. Please make another move."
                col = int(input(player + "'s choice: "))
            self.addMove(col, player)
            i = (i+1)%2
            player = players[i]
            print self

        if (self.winsFor('X')): print "X wins -- Congratulations!"
        elif (self.winsFor('O')): print "O wins -- Congratulations!"
        else:
            print "Board is full -- tie"
        self.clear()
        return
        
            
        

b = Board(7,6)
b.hostGame()
