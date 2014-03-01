def pseudorandom(a,x0,c,m):
    for i in range(10):
        print x0
        x0 = (a*x0+c) % m

pseudorandom(5,6,2,7)
