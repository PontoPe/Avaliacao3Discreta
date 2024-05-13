def rec(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    return (rec(n - 1) * rec(n-2))