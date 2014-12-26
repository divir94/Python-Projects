readFile = open("../Data/Magic Trick Input.txt", "r")
writeFile = open("../Data/Magic Trick Output.txt", "w+")

numInputs = next(readFile)
for num in range(1, int(numInputs)+1):
    i = int(next(readFile))
    #print "Q1: row %s" % i
    for x in range(1,5):
        l = next(readFile)
        if x==i: a = l.split()
    j = int(next(readFile))
    #print "Q2: row %s" % j
    for y in range(1,5):
        l = next(readFile)
        if y==j: b = l.split()
    intersection = [int(x) for x in a if x in b]
    length = len(intersection)
    """
    print a
    print b
    print intersection
    """
    #"""
    if length==1: writeFile.write('Case #%d: %s\n' % (num, intersection[0]))
    elif length>1: writeFile.write('Case #%d: Bad magician!\n' % num)
    elif length==0: writeFile.write('Case #%d: Volunteer cheated!\n' % num)
    #"""

readFile.close()
writeFile.close()
