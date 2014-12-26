# Sort an array. Elements are integers i.e. ages
# Use bucket sort -> array of 0-130 elements
from random import randint
import time

def sort_ages(array):
    d = {}
    t = []
    for i in range(len(array)):
        age = array[i]
        d[age] = d.setdefault(age, 0) + 1

    for i in d.keys():
        for j in range(d[i]):
            t.append(i)
    return t


# Check big-O complexity
elapsed=[]
size = [10, 100, 1000, 10000, 100000, 1000000] # size increases ten times
print "  size ", "time ", "ratio"
for k in range(len(size)):
    array = [randint(0,130) for i in range(size[k])]
    start = time.clock()
    # call function
    sort_ages(array)
    elapsed.append(time.clock() - start)
    if (k): print "%7d"%size[k], "%0.3f"%elapsed[k], "%0.1f"%(elapsed[k]/elapsed[k-1])
    else : print "%7d"%size[k], "%0.3f"%elapsed[k]
