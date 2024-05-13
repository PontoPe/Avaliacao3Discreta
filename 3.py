
def rec(numero):
    if numero == 2:
        return True
    elif numero < 5:
        return False
    else:
        return rec(numero - 3) or rec(numero // 2)



opcoes = [6, 7, 19, 12]

for numero in opcoes:
    if rec(numero):
        print(numero, "pertence a T")
    else:
        print(numero, "não pertence a T")
