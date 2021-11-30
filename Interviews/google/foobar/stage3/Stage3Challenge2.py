"""
Find the Access Codes
=====================

In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading
to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander
Lambda gets a report every day that includes the locks' access codes, but only the Commander knows how to figure out
which of several lists contains the access codes. You need to find a way to determine which list contains the access
codes once you're ready to go in.

Fortunately, now that you're Commander Lambda's personal assistant, Lambda has confided to you that all the access
codes are "lucky triples" in order to make it easier to find them in the lists. A "lucky triple" is a tuple (x, y,
z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list
contains the number of access codes that matches the number of locks on the door when you're ready to go in (for
example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).

Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (
li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.
The elements of l are between 1 and 999999 inclusive.  The solution fits within a signed 32-bit integer. Some of the
lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.

For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the solution 3 total.

"""


def solution(l):
    lengthOfList = len(l)
    numberOfLuckyTriples = 0
    left = 0
    middle = 1
    right = 2
    while True:
        if l[middle] % l[left] == 0:
            if l[right] % l[middle] == 0:
                numberOfLuckyTriples += 1
                if right != lengthOfList - 1:
                    right += 1
                    continue
            else:
                if right != lengthOfList - 1:
                    right += 1
                    continue
        if middle != lengthOfList - 2:
            middle += 1
            right = middle + 1
            continue
        if left != lengthOfList - 3:
            left += 1
            middle = left + 1
            right = middle + 1
            continue
        break
    return numberOfLuckyTriples


def answer(l):
    """
    We start by initializing a counter for every number in the list.
    This counter resembles the number of times a particular entry in the list has been a multiple of a previous number.
    Each time we increment that, we can also increase our number of triplets by the factor we're currently evaluating.
    For example:
    [1, 2, 4, 8]
    When we reach 2, 1 is obviously a factor of 2. c[2] = 1.
    When we reach 4, 1 is a factor of 4. c[4] = 1.
                     2 is a factor of 4. c[4] = 2. triplets += c[2] (triplets is now 1)
    When we reach 8, 1 is a factor of 8. c[8] = 1.
                     2 is a factor of 8. c[8] = 2. triplets += c[2] (triplets is now 2)
                     4 is a factor of 8. c[8] = 3. triplets += c[4]. (triplets is now 4)
    :param l: A list of integers to be evaluated.
    :return: The number of 'lucky triplets' in the given list.
    """
    counts = [0] * len(l)
    triplets = 0
    for product in range(0, len(l)):
        for factor in range(0, product):
            if l[product] % l[factor] == 0:
                counts[product] += 1
                triplets += counts[factor]
    return triplets


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6]
    print(solution(l))
