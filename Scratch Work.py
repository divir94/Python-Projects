#!/usr/bin/python
import numpy as np

size = 8
string = [int(bit) for bit in raw_input().split()]

S = sum(string)

def count_ones(arr):
    return sum(arr)

for end in range(size-1,-1,-1):
    for start in range(end+1):
        middle = string[start : end+1]
        flipped = [int(not(bit)) for bit in middle]
        before = string[:start]
        after = string[end+1:]
        num_ones = count_ones(before + flipped + after)
        if num_ones > S: S = num_ones
print S



