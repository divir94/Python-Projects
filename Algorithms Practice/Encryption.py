# Simple encipher that rotates a word by a certain amount

def encipher(s, n):
    newS =''
    for c in s:
        if 'a' <= c <= 'z':
            neword = ord(c)+n
            if chr(neword) <= 'z':
                newS += chr(neword)
            else:
                newS += chr(neword - 26)
        elif 'A' <= c <= 'Z':
            neword = ord(c)+n
            if chr(neword) <= 'Z':
                newS += chr(neword)
            else:
                newS += chr(neword - 26)
                
        else:
            newS += c
    return newS

print(encipher("Unccl Oveguqnl qhqr! Ubcr lbh unir n jbaqreshy fhzzre va Vaqvn :Q",13))
