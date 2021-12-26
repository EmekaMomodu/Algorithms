"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    # Time complexity O(nlog(n))
    # Space complexity O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True


if __name__ == '__main__':
    s = "cat"
    t = "cat"
    solution = Solution()
    result = solution.isAnagram(s, t)
    print("Result ::: " + result.__str__())

