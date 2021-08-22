"""

  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use the Binary Search algorithm to determine if
  the target integer is contained in the array and should return its index if it
  is, otherwise -1

"""


def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
