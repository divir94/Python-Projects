# Finds max contiguous subarray
# For example, [-2, 1, -3, 4, -1, 2, 1, -5, 4] returns [4, -1, 2, 1] with sum 6.

def max_subarray(A):
    max_ending_here = max_so_far = A[0]
    begin = end = i 0
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

print max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
