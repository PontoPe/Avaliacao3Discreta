def rec(n):
    if n == 1:
        return 10
    return rec(n - 1) + 10

print(rec(5))