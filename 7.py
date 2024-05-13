def bin_odd(n, atual=""):
    if n == 0:
        if atual.count('0') % 2 == 1:
            print(atual)
    else:
        bin_odd(n - 1, atual + '0')
        bin_odd(n - 1, atual + '1')

x = int(input("comprimento dos numeros:"))
bin_odd(x)
