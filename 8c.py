def c(a, b,n):
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        return c(a, b, n - 1) + c(a, b, n - 2)
print(c(1, 2, 5))