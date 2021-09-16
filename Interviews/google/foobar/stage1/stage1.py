def solution(i):
    stringOfPrimes = generateStringOfPrimes(i)
    return stringOfPrimes[i:i+5]


def generateStringOfPrimes(maxStringLengthMinusFive):
    maxStringLength = maxStringLengthMinusFive + 5
    stringOfPrimes = ""
    primes = generatePrimes()
    for prime in primes:
        if len(stringOfPrimes) >= maxStringLength:
            break
        stringOfPrimes += str(prime)
    return stringOfPrimes


def generatePrimes():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


if __name__ == '__main__':
    i = 3
    idx = solution(i)
    print(idx)
