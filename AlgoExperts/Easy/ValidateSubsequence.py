"""

  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers
  <span>[1, 3, 4]</span>
  form a subsequence of the array
  <span>[1, 2, 3, 4]</span>
  , and so do the numbers
  <span>[2, 4]</span>

  . Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

"""

import unittest


def isValidSubsequence(array, sequence):

    sequence_index = 0
    length_of_sequence = len(sequence)

    for number in array:
        if sequence_index < length_of_sequence and number == sequence[sequence_index] :
            sequence_index += 1

    if sequence_index == length_of_sequence:
        return True
    else:
        return False


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence(array, sequence))

"""

Test Case 1
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, 10]
}
Test Case 2
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 25, 6, -1, 8, 10]
}
Test Case 3
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 6, -1, 8, 10]
}
Test Case 4
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [22, 25, 6]
}
Test Case 5
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, 10]
}
Test Case 6
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 10]
}
Test Case 7
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, -1, 8, 10]
}
Test Case 8
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [25]
}
Test Case 9
{
  "array": [1, 1, 1, 1, 1],
  "sequence": [1, 1, 1]
}
Test Case 10
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 12]
}
Test Case 11
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [4, 5, 1, 22, 25, 6, -1, 8, 10]
}
Test Case 12
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 23, 6, -1, 8, 10]
}
Test Case 13
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 22, 25, 6, -1, 8, 10]
}
Test Case 14
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 22, 6, -1, 8, 10]
}
Test Case 15
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, -1]
}
Test Case 16
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, -1, 10]
}
Test Case 17
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, -2]
}
Test Case 18
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [26]
}
Test Case 19
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 25, 22, 6, -1, 8, 10]
}
Test Case 20
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 26, 22, 8]
}
Test Case 21
{
  "array": [1, 1, 6, 1],
  "sequence": [1, 1, 1, 6]
}
Test Case 22
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [1, 6, -1, 10, 11, 11, 11, 11]
}
Test Case 23
{
  "array": [5, 1, 22, 25, 6, -1, 8, 10],
  "sequence": [5, 1, 22, 25, 6, -1, 8, 10, 10]
}

"""