# Find max contiguous subarray
# For example, [5,-7,3,5,-2,4,-1] returns [3,5,-2,4] with sum 10.

def maxSubarray(arr):
    n, result = len(arr), 0
    for i in range(n):
        mySum = 0
        for j in range(i, n):
            mySum += arr[j]
            if mySum > result:
                result = mySum
                start, end = i, j
    return arr[start:end+1], result

def golden_max_subarray(A):
    max_ending = max_subarray = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_subarray = max(max_subarray, max_ending)
    return max_ending, max_subarray

print maxSubarray([5,-7,3,5,-2,4,-1])
print golden_max_subarray([5,-7,3,5,-2,4,-1])
