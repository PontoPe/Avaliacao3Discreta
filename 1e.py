def rec(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    return (((n-1)*rec(n - 1)) + ((n-2)*rec(n-2)))