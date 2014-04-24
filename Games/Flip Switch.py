
# ------------------------ Requires Python 3.0 or more -------------------


"""The goal in Lights On is to turn all of the lights in the initial grid on.
Each time the user selects a light, that light toggles from 0 to 1 or
from 1 to 0. The challenge is that the neighboring light(s) ALSO toggle.
That is, the one, two, three or four lights directly to the N, S, E and W
of the selected light also change state (either on to off, or off to on).
The lights do not "wrap-around": e.g., the leftmost light is not a neighbor
to the rightmost light.

You can play a version of Lights Out here:
http://www.whitman.edu/mathematics/lights_out/"""


from csplot import *
import time # provides time.sleep(0.5)
from random import *  # provides choice( [0,1] ), etc.
import sys # larger recursive stack
sys.setrecursionlimit(100000)  # 100,000 deep
 

 

def runGenerations( L ):
    """ runGenerations keeps running evolve...
    """
    show(L)
    print(L) # display the list, L
    time.sleep(0.5)  # pause a bit
    
    if allOnes(L): return 1
    newL = evolve( L )  # evolve L into newL
    return 1 + runGenerations( newL ) # recurse
 


 

def setNewElement( L, i, x=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    return L[i] + 1

# ----------  Part 0  ------------
# Question 1
def setNewElement( L, i, x=0 ):
    return L[i]**2

# Question 2
def setNewElement( L, i, x=0 ):
    return L[i-1]

# Question 3
def setNewElement( L, i, x=0 ):
    return L[(i+1)%len(L)]

# Random list
def setNewElement( L, i, x=0 ):
    return choice( [0,1] )

# ----------  Part 1  ------------

def allOnes(L):
    for x in L:
        if (x != 1): return False
    return True

# ----------  Part 2  ------------

def setNewElement( L, i, x=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    if i == x: # if it's the user's chosen column,
        return 1- L[i]
    else: # otherwise
        return L[i] # return the original

# ----------  Part 3  ------------
# Question 1


# Question 2
def randBL( N ):
    return [choice([0,1]) for i in range(N)]

# ----------------------------------------------

# Question 3

def runGenerations2d( grid ):
    """ runGenerations keeps running evolve...
    """
    show(grid)
    print(grid) # display the list, L
    time.sleep(0.5)  # pause a bit
    
    if allOnes2d(grid): return 1
    newL = evolve2d( grid )  # evolve L into newL
    return 1 + runGenerations2d( newL ) # recurse
 

def evolve2d( grid):
    """ evolve takes in a list of integers, L,
    and returns a new list of integers
    considered to be the "next generation"
    """
    M = len(grid)
    x, y = sqinput2()  # Get mouse input from the user
    return [ [ setNewElement2d( grid, i, j, x, y) for i in range(M) ] for j in range(M) ]



def setNewElement2d( grid, i, j, x=0, y=0 ):
    """ setNewElement returns the NEW list's ith element
    input L: any list of integers
    input i: the index of the new element to return
    input x: an extra, optional input for future use
    """
    if ((x-1)==i and y==j) or ( ( x==i or (x+1)==i ) and y==j) or (x==i and ( (y-1)==j or (y+1)==j )):
        return 1-grid[j][i]
    return grid[j][i]


def allOnes2d(grid):
    return allOnes([allOnes(x) for x in grid])

def randBL2d(M):
    return [randBL(M) for i in range(M)]

runGenerations2d([[1,0,1],[1,0,0],[0,0,1]])

