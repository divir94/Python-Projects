note = "I love you"
magazine = "There are you a set love love of questions that seem to be commonly-used in interviews and classes when it comes to object-oriented design and analysis"

def note_in_magazine(note, magazine):
    tokens = note.split()
    count = 0
    d = dict.fromkeys(tokens, 0)

    for word in magazine.split():
        if count == len(tokens):
            return True
        if word in d and d[word]==0:
                d[word]=1
                count +=1
    print d
    return False

print note_in_magazine(note, magazine)
