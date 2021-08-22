def getNthFib(n):
    if n == 1 or n == 2:
        return n - 1
    preLast = 0
    last = 1
    for i in range(2, n):
        newLast = preLast + last
        preLast = last
        last = newLast
    return last



