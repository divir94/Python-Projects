from random import randint

def test(numDoors):
    # doors[i] = 1 if car behind door, = 0 if goat behind door
    doors = [0]*numDoors # Initially all doors have a goat
    carIndex = randint(0, len(doors)-1) # get random number
    doors[carIndex] = 1 # add a car behind a random door
    
    choice = doors.pop(randint(0, len(doors)-1)) # choose random door
    for i in range(numDoors-2): doors.remove(0) # numDoors-2 doors with a goat (i.e. 0) is removed

    nochange = choice # player does not switch doors
    change = doors[0] # player switches doors

    return nochange, change

def runTests(repetitions, numDoors):
    noSwitchCount = switchCount = 0

    for i in range(repetitions):
        nochange, change = test(numDoors)
        noSwitchCount += nochange
        switchCount += change

    return noSwitchCount, switchCount

repetitions = int(raw_input("Repetitions: "))
numDoors = int(raw_input("Number of doors: "))
noSwitchCount, switchCount = runTests(repetitions, numDoors)

print "Chance of winning if player does not switch doors: ", 100* (noSwitchCount/ float(repetitions)), "%"
print "Chance of winning if player switches doors: ", 100* (switchCount/ float(repetitions)), "%"
    
