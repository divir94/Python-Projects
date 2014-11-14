d = {
    '2': ['A', 'B', 'C', 'D'],
    '6': ['M', 'N', 'O', 'P'],
    '7': ['P', 'Q', 'R', 'S'],
    '9': ['W', 'X', 'Y', 'Z']
}

def phone_mnemonics(num, remaining, used='', result=[]):
    if len(used) == len(num):
        result.append(used)
        return result
    if not remaining: return

    for char in d[remaining[0]]:
        global count
        count +=1
        phone_mnemonics(num, remaining[1:], used + char, result)

    return result

num = '2276696'
count = 0
print phone_mnemonics(num, num)
print count