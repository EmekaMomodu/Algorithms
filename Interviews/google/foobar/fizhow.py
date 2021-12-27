# time complexity O(n)
# where n = length of input list
# space complexity O(1)
def solution(inputList, targetValue):
    runningSum = 0
    startIndex = 0
    endIndex = 0
    while endIndex < len(inputList):
        runningSum += inputList[endIndex]
        if runningSum == targetValue:
            return [startIndex, endIndex]
        elif runningSum > targetValue:
            runningSum -= inputList[startIndex]
            startIndex += 1
            runningSum -= inputList[endIndex]  # To balance the addition at the start of the loop
            if startIndex > endIndex:
                endIndex = startIndex
        else:
            endIndex += 1
    return [-1, -1]


if __name__ == '__main__':
    inputList = [1, 1, 5, 2, 8]
    targetValue = 15
    result = solution(inputList, targetValue)
    print("Result ::: " + result.__str__())