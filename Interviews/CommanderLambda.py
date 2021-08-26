"""

Commander Lambda uses an automated algorithm to assign minions randomly to tasks, in order to keep minions on their
toes, But you've noticed a flaw in the algorithm -- it eventually loops back on itself, so that instead of assigning new
minions as it iterates, it gets stuck in a cycle of values so that the same minions end up doing the same tasks over and
over again. You think proving this to Commander Lambda will help you make a case for your next promotion.

You have worked out that the algorithm has the following process:

1) Start with a random minion ID n, which is a non negative integer of length k in base b
2) Define x and y as integers of length k. x has the digits of n in descending order, and y has the digits of n in
   ascending order
3) Define z = x - y. Add leading zeros to z to maintain length k if necessary
4) Assign n = z to get the next minion ID, and go back to step 2

For example, given minion ID n = 1211, k = 4, b = 10, then x = 2111, y = 1112 and z = 2111 - 1112 = 0999. Then the next
minion ID will be n = 0999 and the algorithm iterates again: x = 9990, y = 0999 and z = 9990 - 0999 = 8991, and so on.

Depending on the values of n, k (derived from n), and b, at some point the algorithm reaches a cycle, such as by
reaching a constant value. For example, starting with n = 210022, k = 6, b = 3, the algorithm will reach the cycle of
values [210111, 122221, 102212] and it will stay in this cycle no matter how many times it continues iterating. Starting
with n = 1211, the routine will reach the integer 6174, and since 7641 - 1467 is 6174, it will stay as that value no
matter how many times it iterates.

Given a minion ID as a string n representing a non negative integer of length k in base b, where 2 <= k <= 9 and 2 <= b
<= 10, write a function solution(n, b) which returns the length of the ending cycle of the algorithm above starting with
n. For instance, in the example above, solution(210022, 3) would return 3, since iterating on 102212 would return to
210111 when done in base 3. If the algorithm reaches a constant, such as 0, then the length is 1.

"""
import unittest


def solution(n, b):
    listOfIds = [n]
    k = len(n)
    while True:
        x = int(''.join(sorted(n, reverse=True)), b)  # sort n in descending order, covert to base 10, assign value to x
        y = int(''.join(sorted(n)), b)  # sort n in ascending order, covert to base 10, assign value to y
        z = x - y
        # convert z back to base b
        sumOfDigits = -1
        if b != 10:
            z, sumOfDigits = convertBaseTenToBaseB(z, b)
        z = str(z)  # ensure z is a string
        # pad z with leading 0's if z's length doesn't match n
        lengthDifference = k - len(z)
        if lengthDifference:
            while lengthDifference:
                z = '0' + z
                lengthDifference -= 1

        n = z  # new ID (z) created and assigned to n

        lengthOfListOfIds = len(listOfIds)

        # case if 0 valued id is generated i.e n = 00 or 0000 or 000000 ... OR last value of n is same as current value
        if sumOfDigits == 0 or n == listOfIds[-1]:
            return 1

        # search if current value of n has been generated previously, if found then cycle exists, return len of cycle
        for index in range(lengthOfListOfIds):
            currentId = listOfIds[index]
            if n == currentId:
                return lengthOfListOfIds - index

        # if n wasn't found, add to list
        listOfIds.append(n)


def convertBaseTenToBaseB(number, base):
    digits = ''
    sumOfDigits = 0
    while number:
        digit = number % base
        sumOfDigits += digit
        digits = str(digit) + digits
        number = number // base
    return digits, sumOfDigits


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        n = '1211'
        b = 10
        expectedResult = 1
        self.assertEqual(solution(n, b), expectedResult)

    def test_case_2(self):
        n = '210022'
        b = 3
        expectedResult = 3
        self.assertEqual(solution(n, b), expectedResult)
