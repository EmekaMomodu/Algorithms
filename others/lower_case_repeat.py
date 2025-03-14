"""
Write a function solution that, given an integer N, returns a string of length N containing as many different lower-case letters (a' 'z') as possible, in which each letter occurs an equal number of times.
Examples:
1. Given N = 3, the function may return "fig*, "pea*, "nut', etc. Each of these strings contains three
different letters with the same number of occurrences.
2. Given N = 5, the function may return "mango", "grape", "melon", etc.
3. Given N = 30, the function may return "aabbcc...o." (each letter from 'a' to 'o' occurs twice). The
string contains 15 different letters.
Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1.200,000].
"""


def highest_factor_less_than_26(n):
    for i in range(26, 0, -1):
        if n % i == 0:
            return i

def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if N <= 26:
        return alphabet[:N]

    unique_count = highest_factor_less_than_26(N)

    repeat = N // unique_count

    result = alphabet[:unique_count] * repeat

    return result

if __name__ == '__main__':
    N = 20
    print(solution(N))
