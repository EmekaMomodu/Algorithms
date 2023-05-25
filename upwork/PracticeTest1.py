"""
You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

NOTE: + refers to string concatenation.

Example

For s = "xzxzx", the output should be solution(s) = 5.

Consider all the ways to split s into three non-empty parts:

If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
Since there are five valid ways to split s, the answer is 5.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

A string to split.

Guaranteed constraints:
3 ≤ s.length ≤ 100.

[output] integer

The number of ways to split the given string.
"""

"""
The time complexity of the provided implementation of the solution function is O(n^2), where n is the length of the 
input string s. This is because there are two nested loops that iterate over all possible pairs of lengths of 
substrings a and b, and each iteration takes constant time to extract the corresponding substrings and compare their 
concatenations. Therefore, the overall time complexity is proportional to the number of iterations, which is roughly n^2/2.

The space complexity of the function is also O(n), because the only additional memory used is for the three substring 
variables a, b and c, which can each be at most as long as the input string s. Therefore, the total space used is 
proportional to the length of the input string s.
"""

def solution(s):
    n = len(s)
    count = 0
    for len_a in range(1, n - 1):
        for len_b in range(1, n - len_a):
            a = s[:len_a]
            b = s[len_a:len_a+len_b]
            c = s[len_a+len_b:]
            if a+b != b+c and b+c != c+a and c+a != a+b:
                count += 1
    return count
