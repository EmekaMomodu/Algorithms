"""

  Given a non-empty string of lowercase letters and a non-negative integer
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet,
  where k is the key.

  Note that letters should "wrap" around the alphabet; in other words, the
  letter "z"  shifted by one returns the letter "a"

"""


def caesarCipherEncryptor(string, key):
    shiftedString = ""
    key = key % 26
    for char in string:
        shiftedChar = shiftCharByKey(char, key)
        shiftedString += shiftedChar
    return shiftedString


# 97 to 122
def shiftCharByKey(char, key):
    unicode = ord(char)
    shiftedUnicode = unicode + key
    if shiftedUnicode > 122:
        shiftedUnicode = 96 + (shiftedUnicode % 122)
    return chr(shiftedUnicode)
