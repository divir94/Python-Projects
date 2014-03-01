import time

def reverse(n):
    inv = 0
    while (n>0):
        inv = inv*10 + n%10
        n = n/10
    return inv


def DigitComb(low, high):
    largestSoFar = 0
    maxI = maxJ = 0
    for i in range(high, low, -1):
        for j in range(high/11*11, low, -11):
            n = i*j
            if (n>largestSoFar and reverse(n)==n):
                largestSoFar = n
                maxI = i
                maxJ = j
    return largestSoFar, maxI, maxJ

a = time.time()   
print DigitComb(100,999)
print time.time() - a

