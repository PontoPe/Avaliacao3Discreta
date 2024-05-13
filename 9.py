def numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n - 1)

n = int(input("Digite o valor de n: "))
print(n, "-ésimo número triangular:", numero_triangular(n) )
