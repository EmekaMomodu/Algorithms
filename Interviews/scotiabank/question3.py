def solution(s):
    #BANANA 1=B 3=A 2=N
    count_B = s.count('B')
    count_A = s.count('A')
    count_N = s.count('N')

    num_of_moves = min(count_B, count_A // 3, count_N // 2)

    return num_of_moves


if __name__ == '__main__':
    print(solution('NAABXXAN'))
    print(solution('NAABXXAN'))