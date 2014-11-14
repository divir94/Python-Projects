#!/usr/bin/python
import math

d_single_sum = {}
d_multi_sum = {}

def is_square(num): return math.sqrt(num) % 1 == 0

def is_sum_of_sqares(n):
    if n in d_single_sum:
        return d_single_sum[n]
    else:
        for i in range(1, n):
            if is_square(i) and is_square(n-i):
                d_single_sum[n] = i
                return [i, n-i]
    return [-1, -1]

def is_sum_of_k_sqares(num, k):
    if num in d_multi_sum:
        return d_multi_sum[num] == k
    elif k==1:
        return is_square(num)
    else:
        for i in range(1, num):
            if is_sum_of_k_sqares(i, k-1) and is_square(num-i):
                print "num: %d, %d is sum of %d squares and %d is a square" % (num, i, k-1, num-i)
                d_multi_sum[num] = k
                return True
    return False

def min_squares(num):
    for k in range(1, num):
        if is_sum_of_k_sqares(num, k):
            return k
    return num

print min_squares(33)
