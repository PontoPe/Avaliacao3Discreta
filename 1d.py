def rec(n):
    if n == 1:
        return 10
    return (n**2)*rec(n-1) + n - 1
