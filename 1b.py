def rec(n):
    if n == 1:
        return 2
    return ((rec(n - 1)) ** -1)