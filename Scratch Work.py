#!/usr/bin/python

def perm(word, used, remaining, result=[]):
    if len(used) == len(word):
        result.append(used)
        return

    for char in remaining:
        perm(word, used + char, remaining.replace(char, '', 1), result)

    return result


word = 'hello'
print perm(word, '', word, [])
