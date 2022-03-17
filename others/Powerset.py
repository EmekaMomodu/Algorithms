"""
Given a string print all subsets (not permutations)

Eg. String "abc" should output
empty string
a
b
c
ab
bc
ac
abc

"""


def powerSet(array):
    # Write your code here.
    subsets = [[]]
    for element in array:
        for i in range(len(subsets)):
            newSubset = subsets[i] + [element]
            subsets.append(newSubset)
    return subsets
