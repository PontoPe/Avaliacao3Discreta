def rec(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or (n % 2 != 0 and n % 3 != 0):
        return False
    for i in range(2, n):
        if n % i == 0 and rec(i) and rec(n // i):
            return True
    return False


opcoes = [6, 9, 16, 21, 26, 54, 72, 218]


for n in opcoes:
    if rec(n):
        print(n, "pertence a M")
    else:
        print(n, "não pertence a M")
