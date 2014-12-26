import glob, os, heapq
malePath = '/Users/Divir/Desktop/names/m/'
namePaths = glob.glob(malePath+'*') # get all file paths under male ('m') folder 

# Make a dictionary with (key, value) = (name, frequency)
# Details:
# x.startswith('.') is to avoid some hidden system files that start with a dot like '.DS_Store'
myDict = dict([ ( os.path.split(path)[1], len( [x for x in os.listdir(path) if not x.startswith('.')] ) ) for path in namePaths])

# Alternatively, you could do this (which is equivalent) -
"""
myDict = {}
for path in namePaths:
    name = os.path.split(path)[1]
    numFiles = len( [f for f in os.listdir(path) if not f.startswith('.')] )
    myDict[name] = numFiles
"""

topN = 10
popularNames = heapq.nlargest(topN, myDict, key=myDict.get)

# Again, you could do this instead  -
"""
for i in range(min(10, len(myDict))):
    popular = max(myDict, key=myDict.get)
    print popular
    del myDict[popular]
"""

print myDict
print popularNames
