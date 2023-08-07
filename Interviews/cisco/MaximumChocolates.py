"""
There is a set of N jars containing chocolates Some of them may be empty. Determine the maximum number of chocolates Andrew can pick from the jars given that he cannot pick from Jars next to each other.
Write an algorithm to find the maximum number of chocolates that can be picked from the jars in such a way that the chocolates are not picked from jars next to each other.
Input
The first line of input consists of an integer-numjars, representing the number of jars (N).
The next line consists of N space-separated integers representing the number of chocolates in each jar.
Output
Print the maximum number of chocolates that can be picked from the jars in such a way that the chocolates are not picked from jars next to each other.
Constraints
1€ N <= 1000
Example
Input:
6
5 30 99 60 5 10
Output:
114
Explanation:
Andrew picks from the 1st (5), 3rd (99) and 6th
(10) jars.
So, the output is 114.
ChatGPT


"""

"""
To find the maximum number of chocolates that Andrew can pick from the jars in such a way that he cannot pick from jars next to each other, you can use a dynamic programming approach.

Here's the algorithm to solve the problem:

    Read the input N (the number of jars).
    Read the N space-separated integers representing the number of chocolates in each jar.
    Create a list dp of length N to store the maximum number of chocolates that can be picked from jars in such a way that the chocolates are not picked from jars next to each other.
    Initialize dp[0] with the number of chocolates in the first jar.
    Initialize dp[1] with the maximum of the number of chocolates in the first and second jars.
    For each jar from the third jar (index 2) to the last jar (index N-1):
    a. Calculate dp[i] as the maximum of dp[i-1] (maximum number of chocolates picked so far) and dp[i-2] + chocolates in the current jar (as Andrew cannot pick from jars next to each other).
    The maximum number of chocolates that can be picked is dp[N-1].
    Print the maximum number of chocolates.
"""

def maximum_chocolates(numjars, jars):
    if numjars == 0:
        return 0

    if numjars == 1:
        return jars[0]

    dp = [0] * numjars
    dp[0] = jars[0]
    dp[1] = max(jars[0], jars[1])

    for i in range(2, numjars):
        dp[i] = max(dp[i-1], dp[i-2] + jars[i])

    return dp[numjars-1]

# Read input
numjars = int(input())
jars = list(map(int, input().split()))

# Calculate and print the maximum number of chocolates that can be picked
result = maximum_chocolates(numjars, jars)
print(result)

