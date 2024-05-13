def a(n):
    if n == 1:
        return 1
    else:
        return 3 * a(n - 1)
print(a(3))