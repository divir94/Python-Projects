# Determine the second frequent number in an input array

def 2nd_mode(inp):
    d = {}
    # if key in dict increment, otherwise add with val=1
    for x in inp: d[x] = d.setdefault(x, 0) + 1
    # find max value and return its key
    mode = max(d, key=d.get)
    # remove mode and return next mode
    d.pop(mode)
    return max(d, key=d.get)

print find_mode([1,2,3,3,3,2])
