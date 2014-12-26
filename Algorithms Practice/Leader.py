# A leader of a sequence is the element whose value occurs more than
# n/2 times. returns leader if it exists, -1 otherwise.

def leader(arr):
    mydict = {}
    for x in arr:
        mydict[x] = mydict.setdefault(x, 0) + 1
    mode = max(mydict, key=mydict.get)
    if mydict[mode] > len(arr)/2: return mode
    return -1

print leader([6,8,4,6,6])
