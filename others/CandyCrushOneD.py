"""
Write a function to crush candy in one dimensional board. In candy crushing games, groups of like items are removed from
the board. In this problem, any sequence of 3 or more like items should be removed and any items adjacent to that
sequence should now be considered adjacent to each other. This process should be repeated as many time as possible. You
should greedily remove characters from left to right.

Example 1:

Input: "aaabbbc"
Output: "c"
Explanation:
1. Remove 3 'a': "aaabbbbc" => "bbbbc"
2. Remove 4 'b': "bbbbc" => "c"
Example 2:

Input: "aabbbacd"
Output: "cd"
Explanation:
1. Remove 3 'b': "aabbbacd" => "aaacd"
2. Remove 3 'a': "aaacd" => "cd"
Example 3:

Input: "aabbccddeeedcba"
Output: ""
Explanation:
1. Remove 3 'e': "aabbccddeeedcba" => "aabbccdddcba"
2. Remove 3 'd': "aabbccdddcba" => "aabbcccba"
3. Remove 3 'c': "aabbcccba" => "aabbba"
4. Remove 3 'b': "aabbba" => "aaa"
5. Remove 3 'a': "aaa" => ""
Example 4:

Input: "aaabbbacd"
Output: "acd"
Explanation:
1. Remove 3 'a': "aaabbbacd" => "bbbacd"
2. Remove 3 'b': "bbbacd" => "acd"

"""
import unittest


def candy_crush(inputString):
    if not inputString:
        return inputString

    stack = [[inputString[0], 1]]

    for i in range(1, len(inputString)):
        if inputString[i] != inputString[i - 1]:
            if stack[-1][1] >= 3:
                stack.pop()
            if stack and stack[-1][0] == inputString[i]:
                stack[-1][1] += 1
            else:
                stack.append([inputString[i], 1])
        else:
            stack[-1][1] += 1

    # handle end
    if stack[-1][1] >= 3:
        stack.pop()

    out = []
    for items in stack:
        out += items[0] * items[1]

    return ''.join(out)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        inputString = 'aaaabbbc'
        expectedResult = 'c'
        self.assertEqual(candy_crush(inputString), expectedResult)

    def test_case_2(self):
        inputString = 'aabbbacd'
        expectedResult = 'cd'
        self.assertEqual(candy_crush(inputString), expectedResult)
