def b(n):
    if n == 1:
        return 2
    else:
        return b(n - 1) / 2
print(b(4))