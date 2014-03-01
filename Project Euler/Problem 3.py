# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
t = []
def factors(n):
    if (n==1): return
    i=2
    root = int(sqrt(n)+2) # Check only till sqrt(n)
    while (i<=root and n%i): # increment if not divisible by i
        i+=1
    if (i>=root): t.append(n)
    elif (not(n%i)): # if i divides n, it's a factor, add it
        t.append(i)
        return factors(n/i)
    return 

factors(600851475143)
print max(t)
    
