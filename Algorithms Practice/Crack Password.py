import string
import itertools


def guess_pass():
    letters = list(string.lowercase)
    numbers = [str(x) for x in range(10)]
    alpha_numeric = letters + numbers
    guess = ""
    
    for word in itertools.product(alpha_numeric, repeat=4):
        if ''.join(word) == password:
            guess = ''.join(word)
            
    print "Hacked it!\nPassword is %s" % guess if guess else "Failed to crack password :(" 


password = '7hot'
guess_pass()
