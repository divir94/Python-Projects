# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.


def SumEvenFib(x0, x1, mysum):
    x2 = x0 + x1
    if (x2>=4000000): return mysum
    if (not x2%2): mysum += x2
    return SumEvenFib(x1, x2, mysum)


print SumEvenFib(1,1,0)
    
