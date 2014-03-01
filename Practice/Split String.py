# Split input string with a given delimiter

def my_split(inp, sep):
    s = list(inp)
    count = 0
    for x in s:
        if (x == sep): count += 1
    for i in range(count): s.remove(sep)
    return "".join(s)


print my_split("a  b c dc dref d sd ewf rf s d", " ")

