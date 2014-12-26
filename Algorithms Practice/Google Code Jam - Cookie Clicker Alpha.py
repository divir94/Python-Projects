readFile = open("../Data/Cookie Clicker Input.txt", "r")
writeFile = open("../Data/Cookie Clicker Output.txt", "w+")

def cookieClicker(C, F, X):
    farmYield = 2.0
    timeWait = X/farmYield
    timeBuyFarm = C/farmYield + X/(farmYield + F)
    totalTime = 0

    while timeBuyFarm < timeWait:
        totalTime += C/farmYield
        #print "timeBuyFarm: %d, timeWait: %d, extraTime: %d, totalTime: %d" % (timeBuyFarm, timeWait, C/farmYield, totalTime)
        farmYield += F
        timeWait = X/farmYield
        timeBuyFarm = C/farmYield + X/(farmYield + F)
    return totalTime + X/(farmYield)
      

numInputs = next(readFile)
for num in range(1, int(numInputs)+1):
    inp = next(readFile).split()
    C, F, X = float(inp[0]), float(inp[1]), float(inp[2])
    # Write to file
    writeFile.write('Case #%d: %.7f\n' % (num, cookieClicker(C, F, X)))

readFile.close()
writeFile.close()
