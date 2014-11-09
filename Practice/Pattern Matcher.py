'''
pattern = "abba"
match = "yoheyheyyo"
'''

def wordpattern(pattern,  match):
    #print "Pattern: %s, Match: %s" % (pattern, match)

    if pattern == "" and match == "":
        return 1
    if pattern == "" or match == "":
        return 0

    for i in range(1, len(match)+1):
        pat = pattern[0]
        x = match[:i]

        if pat in d:
            if match.find(d[pat]) != 0: return 0
            return wordpattern(pattern[1:], match.replace(d[pat], '', 1))

        else:
            d[pat] = x
            if wordpattern(pattern.replace(pat, '', 1), match.replace(x, '', 1)) \
                    and len(d.values()) == len(set(d.values())):
                return 1

        d.pop(pat, None)

    return 0

d = {}
pattern = "abcdeeee"
match = "onetwothreefourcowcowcowcow"

print wordpattern(pattern, match)
print d



