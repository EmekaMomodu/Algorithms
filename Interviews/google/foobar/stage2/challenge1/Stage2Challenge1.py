def solution(l):
    l.sort(reverse=True)
    sumOfAllDigits = sum(l)
    remainder = sumOfAllDigits % 3
    if remainder == 0:
        return convertListToInteger(l)
    listLength = len(l)
    index = listLength - 1
    if remainder == 1:
        validResult = handleRemainderOne(l, index)
        if validResult:
            return validResult
    elif remainder == 2:
        validResult = handleRemainderTwo(l, index)
        if validResult:
            return validResult
    return 0


def handleRemainderOne(list_, index):
    remainderOfTwo = [-1, -1]
    while index >= 0:
        remainder = list_[index] % 3
        if remainder == 1:
            list_.pop(index)
            return convertListToInteger(list_)
        if remainder == 2:
            if remainderOfTwo[0] == -1:
                remainderOfTwo[0] = index
            elif remainderOfTwo[1] == -1:
                remainderOfTwo[1] = index
        index -= 1
    if len(remainderOfTwo) == 2:
        list_.pop(remainderOfTwo[0])
        list_.pop(remainderOfTwo[1])
        return convertListToInteger(list_)
    return 0


def handleRemainderTwo(list_, index):
    remainderOfOne = [-1, -1]
    while index >= 0:
        remainder = list_[index] % 3
        if remainder == 2:
            list_.pop(index)
            return convertListToInteger(list_)
        if remainder == 1:
            if remainderOfOne[0] == -1:
                remainderOfOne[0] = index
            elif remainderOfOne[1] == -1:
                remainderOfOne[1] = index
        index -= 1
    if len(remainderOfOne) == 2:
        list_.pop(remainderOfOne[0])
        list_.pop(remainderOfOne[1])
        return convertListToInteger(list_)
    return 0


def convertListToInteger(list_):
    return sum(digit * 10 ** i for i, digit in enumerate(list_[::-1]))


if __name__ == '__main__':
    l = [3, 1, 4, 1, 5, 9]
    print(solution(l))
