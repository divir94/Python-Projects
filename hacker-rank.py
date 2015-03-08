from math import factorial

def is_palindrome(str, n, even):
    if even:
        return str[:n/2] == str[-1:(n/2)-1:-1]
    else:
        return str[:n/2] == str[-1:(n/2):-1]

def freq_dict(str):
    d = {}
    for char in str:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d

def num_palindromes(str):
    dict = freq_dict(str)
    den = 1
    num_pairs = 0
    for val in dict.values():
        num = val/2
        num_pairs += num
        den = den * factorial(num)
    return int(factorial(num_pairs)/float(den))

print num_palindromes('cdcdcdcdeeeef')