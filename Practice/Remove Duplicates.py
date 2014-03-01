# Remove duplicate items in an array

def remove_duplicates(inp):
    d = {}
    for x in inp:
        if (x not in d): d[x] = True
        else: inp.remove(x)
    return inp

        
def mode(inp):
    mydict = {}
    for x in inp:
       mydict[x] = mydict.setdefault(x, 0) + 1
    return max(mydict, key=mydict.get)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print remove_duplicates(basket)

#print(mode([5,5,3,4,6,4]))
