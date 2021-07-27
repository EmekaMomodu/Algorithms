"""

  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.


"""

from collections import deque
import unittest


def sortedSquaredArray(array):
    sortedSquares = deque()

    leftPointer = 0
    rightPointer = len(array) - 1

    while leftPointer <= rightPointer:
        absoluteLeftNumber = abs(array[leftPointer])
        absoluteRightNumber = abs(array[rightPointer])

        if leftPointer == rightPointer:
            nextSquaredArrayItem = absoluteLeftNumber ** 2
            sortedSquares.appendleft(nextSquaredArrayItem)
            break

        if absoluteLeftNumber < absoluteRightNumber:
            nextSquaredArrayItem = absoluteRightNumber ** 2
            sortedSquares.appendleft(nextSquaredArrayItem)
            rightPointer -= 1

        elif absoluteLeftNumber > absoluteRightNumber:
            nextSquaredArrayItem = absoluteLeftNumber ** 2
            sortedSquares.appendleft(nextSquaredArrayItem)
            leftPointer += 1

        else:
            nextSquaredArrayItem = absoluteLeftNumber ** 2
            sortedSquares.appendleft(nextSquaredArrayItem)
            sortedSquares.appendleft(nextSquaredArrayItem)
            leftPointer += 1
            rightPointer -= 1

    return list(sortedSquares)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [1, 2, 3, 5, 6, 8, 9]
        expected = [1, 4, 9, 25, 36, 64, 81]
        actual = sortedSquaredArray(input)
        self.assertEqual(actual, expected)


"""
Test Case 1
{
  "array": [1, 2, 3, 5, 6, 8, 9]
}
Test Case 2
{
  "array": [1]
}
Test Case 3
{
  "array": [1, 2]
}
Test Case 4
{
  "array": [1, 2, 3, 4, 5]
}
Test Case 5
{
  "array": [0]
}
Test Case 6
{
  "array": [10]
}
Test Case 7
{
  "array": [-1]
}
Test Case 8
{
  "array": [-2, -1]
}
Test Case 9
{
  "array": [-5, -4, -3, -2, -1]
}
Test Case 10
{
  "array": [-10]
}
Test Case 11
{
  "array": [-10, -5, 0, 5, 10]
}
Test Case 12
{
  "array": [-7, -3, 1, 9, 22, 30]
}
Test Case 13
{
  "array": [-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20]
}
Test Case 14
{
  "array": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}
Test Case 15
{
  "array": [-1, -1, 2, 3, 3, 3, 4]
}
Test Case 16
{
  "array": [-3, -2, -1]
}
Test Case 17
{
  "array": [-3, -2, -1]
}

"""