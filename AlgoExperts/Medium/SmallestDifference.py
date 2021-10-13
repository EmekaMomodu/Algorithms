"""

  Write a function that takes in two non-empty arrays of integers, finds the
  pair of numbers (one from each array) whose absolute difference is closest to
  zero, and returns an array containing these two numbers, with the number from
  the first array in the first position.

  Note that the absolute difference of two integers is the distance between
  them on the real number line. For example, the absolute difference of -5 and 5
  is 10, and the absolute difference of -5 and -4 is 1.

  You can assume that there will only be one pair of numbers with the smallest
  difference.

"""


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    firstIdx = 0
    secondIdx = 0

    firstLen = len(arrayOne)
    secondLen = len(arrayTwo)

    smallestDifference = float('inf')

    while firstIdx < firstLen and secondIdx < secondLen:
        first = arrayOne[firstIdx]
        second = arrayTwo[secondIdx]
        currentDifference = abs(first - second)
        if currentDifference < smallestDifference:
            smallestDifference = currentDifference
            smallestDifferenceArray = [first, second]
        if first == second:
            return smallestDifferenceArray
        elif first < second:
            firstIdx += 1
        elif second < first:
            secondIdx += 1

    return smallestDifferenceArray
