def d(p, q, n):
    if n == 1:
        return p
    elif n == 2:
        return p - q
    elif n % 2 == 0:
        return (d(p, q, n - 1)) * -1 + p
    else:
        return d(p, q, n - 1) + q


print(d(1, 2, 5))