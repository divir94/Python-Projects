##[a-zA-Z0-9]
##
##encode(abcccccccccftcc) = ab9xcft2xc     ab9xcftcc
##decode(ab9xcftcc)
##
##encode(ab5xt) = ab5xt = ab1x51xxt
##
##decode(ab51xxt) = abxxxxxxxxxxx...xxxt
##decode(ab5xt) = abttttt
##
##encode(ab5xt) = ab
##
##
##encode(a) = a
##encode(a) = 
##
##abccc

def encode(s):
    length = len(s)-1
    if length < 3: return s
    
    i, news = 0, ''
    while i < length:
        num = 0
        c, nextc = s[i], s[i+1]
        
        while ( nextc == c  and  i < length ):
            c, nextc = s[i], s[i+1]
            num, i  = num+1, i+1
            
        if num>0: news += str(num) + 'x' + c
        else: news += c 
        i += 1
            
    return news

print encode('aabbbbbb')
    
