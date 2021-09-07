"""

  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.

"""


def isPalindrome(string):
    leftPointer = 0
    rightPointer = len(string) - 1
    while leftPointer <= rightPointer:
        if string[leftPointer] != string[rightPointer]:
            return False
        leftPointer += 1
        rightPointer -= 1
    return True
