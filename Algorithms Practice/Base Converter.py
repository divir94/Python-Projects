# Converts from any base to any other base b/w 2-36

# eg. toBase(17,2) -> 10001 (base 2)
def toBase(num, base_b):
    """Convert from a common base to base_b"""
    digits = []
    while (num>0):
        digit = num % base_b
        # digit -> character, e.g. 10 -> 'a', 35 -> 'z'
        if (10<=digit<=36): digit = chr(ord('a')+digit-10)          
        digits.insert(0, str(digit))
        num = num/base_b
    return "".join(digits)

# eg. fromBase('11',16) -> 17 (base 10)
def fromBase(num, base_a):
    """Convert from base_a to a common base"""
    digits = [character for character in num]
    num = 0
    for digit in digits:
        # character -> digit, e.g. 'a' -> '10, 'z' -> 35
        if ('a'<=digit<='z'): digit = ord(digit)-ord('a')+10
        num =  num*base_a + int(digit)
    return num

# Converts num from base_a to base_b
# e.g. convertBase('11', 16, 2 ) -> 10001
# '11'(base 16) = 17 (base 10) = 10001 (base 2)
def convertBase(num, base_a, base_b):
    """Convert the num from base_a to base_b"""
    return toBase(fromBase(num, base_a), base_b)
    
#print fromBase('11',16)
#print toBase(17,2)
print convertBase('11',16,2)

print toBase(125, 62)