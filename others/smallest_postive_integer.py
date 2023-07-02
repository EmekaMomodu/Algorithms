"""
This is a demo task.
Write a function:
def solution (A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.
Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1.. 100,000);
each element of array A is an integer within the range [-1,000,000.. 1,000,000].

"""


def solution(A):
    # Filter out non-positive integers and duplicates
    A = set([a for a in A if a > 0])
    # Check for the smallest positive integer that does not occur in A
    smallest = 1
    while smallest in A:
        smallest += 1
    return smallest

# sort array
#     A.sort()
#     # initialise variable for tracking current smallest positive integer
#     current_smallest_positive_integer = 1
#     # initialise loop counter
#     idx = 0
#     # traverse array until a positive value is encountered
#     while idx < len(A):
#         if A[idx] < 0:
#             idx += 1
#             continue
#     # keep traversing until a different value from previous value is encountered
#         while idx < len(A) A[idx]
#     # check if value is not equal to current smallest positive integer
#     # return current smallest positive integer
