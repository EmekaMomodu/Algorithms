"""
    Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.
    Example 2:

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
    Example 3:

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


    Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""

# Solution 1
class SolutionOne:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        currentLongestLength = 0
        hashMap = {}
        pointer = 0
        while pointer < len(s):
            currentChar = s[pointer]
            indexSavedInHashMap = hashMap.get(currentChar, -1)
            isCurrCharOutsideCurrSubStr = True if pointer - currentLongestLength > indexSavedInHashMap else False
            if indexSavedInHashMap < 0 or indexSavedInHashMap == pointer or isCurrCharOutsideCurrSubStr:
                hashMap[currentChar] = pointer
                pointer += 1
                currentLongestLength += 1
            else:
                hashMap[currentChar] = pointer
                pointer = indexSavedInHashMap + 1
                longestLength = max(currentLongestLength, longestLength)
                currentLongestLength = 0
        longestLength = max(currentLongestLength, longestLength)
        return longestLength if longestLength != 0 else currentLongestLength


# Solution 2 SLIDING WINDOW  ---inputString <-> s
class SolutionTwo:
    def lengthOfLongestSubstring(self, inputString: str) -> int:
        longestLength = 0
        hashMap = {}
        leftPointer = 0
        for rightPointer in range(len(inputString)):
            currentChar = inputString[rightPointer]
            if currentChar in hashMap:
                prevIndex = hashMap[currentChar]
                leftPointer = max(leftPointer, prevIndex + 1)
            longestLength = max(longestLength, rightPointer - leftPointer + 1)
            hashMap[currentChar] = rightPointer
        return longestLength





