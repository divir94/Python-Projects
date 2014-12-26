# Remove duplicate items in an array

def remove_duplicates(inp):
    out = []
    for x in inp:
        if x not in out: out.append(x)
    return out

        
def mode(inp):
    mydict = {}
    for x in inp:
       mydict[x] = mydict.setdefault(x, 0) + 1
    return max(mydict, key=mydict.get)

print remove_duplicates([2,2,5,5])
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print remove_duplicates(basket)

#print(mode([5,5,3,4,6,4]))
