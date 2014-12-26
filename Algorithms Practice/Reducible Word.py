# http://www.greenteapress.com/thinkpython/thinkpython.pdf
# Exercise 12.6

def make_word_dict():
    d = dict()
    fin = open('../Data/English Wordlist.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word
    return d

"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

memo = dict()
memo[''] = ''

def children(word, word_dict):
    res = []
    for i in range(len(word)):
        child = word[:i] + word[i+1:]
        if child in word_dict:
            res.append(child)        
    return res

def is_reducible(word, word_list):
    if word in memo:
        return memo[word]

    res = []
    for child in children(word, word_dict):
        t = is_reducible(child, word_dict)
        if t != []:
            res.append(child)

    memo[word] = res
    return res

def all_reducibles(word_list):
    words = []
    for word in word_list:
        t = is_reducible(word, word_dict)
        if t != []:
            words.append((len(word), word))
            
    return words

def print_long_reducibles(word_list):
    words = all_reducibles(word_list)
    words.sort(reverse = True)
    for length, word in words[:5]:
        print length,
        print_order(word)
        print '\n'
        
def print_order(word):
    if len(word) == 0: return
    print word,
    child = is_reducible(word, word_dict)
    print_order(child[0])

word_dict = make_word_dict()
print_long_reducibles(word_dict)

#print_order('ambulance', word_dict)
