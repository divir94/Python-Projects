def reverseInt(num):
    reverse=negative = 0
    if(num<0):
        num = -1*num
        negative = 1
    while (num>0):
        digit = num%10
        reverse = reverse*10 + digit
        num = (num-digit)/10
    if negative: return -1*reverse
    return reverse

#print reverseInt(-123)


def int2words(num):
    mydict = {1:'one', 3:'three',20:'twenty', 100:'hundred'}
    words = ''
    i=1
    while (num>0):
        digit = num%(10**i)
        print digit, mydict[digit]
        num = num-digit
        i += 1
int2words(123)
        
