"""

  Write a function that takes in an array of at least three integers and,
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.


"""


import unittest


def findThreeLargestNumbers(array):
    threeLargestNumbers = [None, None, None]
    for number in array:
        index = 2
        while index >= 0:
            print("current number: " + str(number))
            oneLargeNumber = threeLargestNumbers[index]
            print("current Large Number: " + str(oneLargeNumber))
            if oneLargeNumber is None:
                threeLargestNumbers[index] = number
                break
            if number >= oneLargeNumber:
                if index == 2:
                    threeLargestNumbers[0] = threeLargestNumbers[1]
                    threeLargestNumbers[1] = threeLargestNumbers[2]
                    threeLargestNumbers[2] = number
                elif index == 1:
                    threeLargestNumbers[0] = threeLargestNumbers[1]
                    threeLargestNumbers[1] = number
                else:
                    threeLargestNumbers[0] = number
                break
            index -= 1
        print(threeLargestNumbers)
    return threeLargestNumbers


if __name__ == "__main__":
    array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
    result = findThreeLargestNumbers(array)
    print("result::: " + str(result))


class TestProgram(unittest.TestCase):
    def testCase1(self):
        array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
        expectedResult = [18, 141, 541]
        self.assertEqual(findThreeLargestNumbers(array), expectedResult)
