def look_and_say(num):
    count = 0
    i = 1
    result = ''
    prev = num[0]

    for char in num+'0':
        #print 'prev: %s, char: %s, count: %d' % (prev, char, count)
        if prev != char:
            result += str(count) + prev
            count = 0
        prev = char
        count += 1

    return result

def look_and_say_series(n):
    result = ['1']
    for i in range(n):
        result.append(look_and_say(result[-1]))
    return result

print look_and_say('aaaabcccaa')

