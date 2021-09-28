"""

  Write a function that takes in a string of lowercase English-alphabet letters
  and returns the index of the string's first non-repeating character.

  The first non-repeating character is the first character in a string that
  occurs only once.

  If the input string doesn't have any non-repeating characters, your function
  should return

"""


def firstNonRepeatingCharacter(string):
    counts = {}
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    for index in range(len(string)):
        char = string[index]
        count = counts[char]
        if count == 1:
            return index
    return -1
