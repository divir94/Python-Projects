# Convert string to int without using built in methods
# like string.atoi or int()

def string2Int(num_str):
    my_sum, base = 0, ord('0')
    reverse_num_str  = num_str[::-1]
    for i in range(len(num_str)):
        my_sum += (ord(reverse_num_str[i]) - base) *(10**i)
    return my_sum

def oneLineString2Int(num_str):
    return sum([(ord(n)-ord('0')) *(10**i) for i,n in enumerate(reversed(num_str))])

print oneLineString2Int('1224')
