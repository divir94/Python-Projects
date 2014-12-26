# Reads a file and scrambles each word, leaving the first and last letters
# unchanged, and writes back to another file.

from random import shuffle
readFile = open("../Data/Piedpiper.txt", "r")
writeFile = open("../Data/Scrambled Piedpiper.txt", "w")

def scrambleWord(word):
    if(len(word)<3): return word
    newWord=word
    word = list(word[1:-1])
    shuffle(word)
    newWord= [newWord[0]] + word + [newWord[-1]]
    return "".join(newWord)

wordList = []

for line in readFile:
    for word in line.split():
        wordList.append(scrambleWord(word))
    wordList= " ".join(wordList)
    #print(wordList)
    writeFile.write(wordList)
    writeFile.write('\n')
    wordList = []

readFile.close()
writeFile.close()



