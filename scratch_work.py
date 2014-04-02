##[1,2,3]
##1,2
##1,3
##2,3
##
##1,1  1,2  1,3
##2,1  2,2  2,3
##3,1  3,2  3,3

def sum_pairs(inp):
    d = {}
    di = {}
    for i in inp:
        for j in inp:
            if ((i != j) and ((j,i) not in d)):
                mysum = i+j
                print i, j, " sum: ", mysum
                if mysum in di:
                    di[mysum].append((i,j))
                else: di[mysum] = [(i,j)]
            d[(i,j)]=True
    for key in di:
        print "key: ", key, "value: ", di[key]

sum_pairs([1,2,3,4,5])
