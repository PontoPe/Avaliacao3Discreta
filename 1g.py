def rec(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    return (rec(n - 1) + (2 * rec(n-2)) + (3 * rec(n-3)))