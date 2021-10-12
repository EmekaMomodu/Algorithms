"""

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.

"""


def threeNumberSum(array, targetSum):
    threeNumberSumArray = []
    array.sort()
    arrayLength = len(array)
    for i in range(arrayLength - 2):
        currentNumber = array[i]
        left = i + 1
        right = arrayLength - 1
        while left < right:
            currentSum = currentNumber + array[left] + array[right]
            if currentSum == targetSum:
                threeNumberSumArray.append([currentNumber, array[left], array[right]])
                right -= 1
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return threeNumberSumArray

