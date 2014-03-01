# Print all permutations of a string

def perm(inp):
    if (len(inp) <= 1):
        print inp
        return [inp]
    wordlist = perm( inp[:-1] )
    c = inp[-1]
    t = []
    for word in wordlist:
        for i in range(len(word)+1):
            new_word = word[:i] + c + word[i:]
            t.append(new_word)
            print new_word
    return t

perm('hello')
