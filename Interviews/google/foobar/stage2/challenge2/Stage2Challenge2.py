def solution(s):
    salutes = 0
    countEmployeeToSalute = 0
    for employee in s:
        if employee == '>':
            countEmployeeToSalute += 1
        elif employee == '<':
            currentSalutes = countEmployeeToSalute * 2
            salutes += currentSalutes
    return salutes


if __name__ == '__main__':
    s = "<<>><"
    print(solution(s))