# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def SumDivisibleBy(x):
    n = 999/x           #number of numbers in 999 that are divisible by x
    return x*n*(n+1)/2

def multiples(n):
    return SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)
              
print multiples(999)
    
# Two-liner
f = lambda a, n, d: (n * (2 * a + (n - 1) * d)) / 2
print f(3, 999 / 3, 3) + f(5, 999 / 5, 5) - f(15, 999 / 15, 15)
