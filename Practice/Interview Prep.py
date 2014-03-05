def reverse(mystr):
    mystr = list(mystr)
    for i in range(len(mystr)/2):
        temp = mystr[i]
        mystr[i] = mystr[-i-1]
        mystr[-i-1] = temp
    return "".join(mystr)

#print reverse('abc')


mydict = {}
def fib(n):
    if (n<=1): return n
    mydict[n] = mydict.setdefault(n, fib(n-1) + fib(n-2));
    return mydict[n]

#for i in range(11): print fib(i)

def multiplication_table(low, high):
    t = range(low, high+1)
    for i in range(low, high+1):
        print ["%3d"%(i*x) for x in t]

#multiplication_table(1,12)

def isInt(value):
  try:
    int(value)
    return int(value)
  except ValueError:
    return None

#print isInt('a')

def printOdd(low, high):
    for num in range(low, high+1,2):
        print num

#printOdd(1,9)

def largestVal(arr):
    size = len(arr)
    if (size<=1): return arr
    largest = arr[0]
    for num in arr:
        if num>largest: largest = num
    return largest

#print largestVal([5,2,12,5,2])

def rgb(r,g,b): return hex(r)+hex(g)[2:]+hex(b)[2:]

#print rgb(255, 0, 128)

def insertBits(N, M, i, j):
    clearMask = ((1<<(j-i+1))-1) << i    # 000011110000, 1s from i to j
    # clears bits fron i to j
    N = N & ~clearMask
    # shift M by i to insert at the right place
    maskM = M << i
    N = N | maskM
    return N

#print bin(insertBits(1<<10, 19, 2, 4))

def getSign(num): return (num>>31)&1

#for i in range(-5,5): print i, getSign(i)


def popCount(num):
    count = 0
    for i in range(32):
        count += num&1
        num = num>>1
    return count

#print popCount(0)

def getBit(num,i):
    return (num & 1<<i) != 0

def isPalindrome(num):
    start=0; end=32
    while (end>start):
        if (getBit(num,start)!=getBit(num,end)): return False
        start+=1; end-=1
    return True

#print isPalindrome((1<<16)&(1<<13))

class queue:
    def __init__(self, size):
        self.size=size
        self.arr = size*[None]
        self.i = 0

    def enqueue(self, item):
        self.arr[self.i] = item
        self.i = (self.i+1) % self.size
        print self.arr

    def dequeue(self):
        item = self.arr[self.i]
        self.i = (self.i-1) % self.size
        print self.arr
        return item

##q = queue(4)
##q.enqueue(1)
##q.enqueue(2)
##q.dequeue()
##q.enqueue(3)
##q.enqueue(4)

def binarySearch(t,x, low, high):
    while (high >= low):
        mid = (high+low)/2
        if (t[mid] == x): return mid
        elif (x > t[mid]): low = mid+1
        else: high = mid-1
    return False

##t = [1]
##t.sort()
##print t
##print binarySearch(t, 2, 0, len(t)-1)

def check_row(t):
    myDict = {}
    keys = [i for i in range(10)]
    vals = [1 for i in keys]
    validDict = dict(zip(keys,vals))
    for x in t:
        myDict[x] = myDict.setdefault(x, 0) + 1
    print validDict
    print myDict
    return myDict == validDict

t = [1,2,4,3,5,6,7,8,9,0]
print check_row(t)
    
