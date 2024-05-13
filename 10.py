def colonia(n):
    if n == 0:
        return 50000
    else:
        return (3 * colonia(n - 1))

print(colonia(1))
cont = 0 
populacao = 50000
while populacao <= 153450026:
    cont += 1
    populacao = colonia(cont)
print(f"{cont} anos.")