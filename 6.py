def rec(letras):
    if letras == 'a' or letras == 'b' or letras == 'c':
        return True
    
    if len(letras) > 1 and (letras.endswith('a') or letras.endswith('b') or letras.startswith('c') or letras.startswith('b') or (letras.endswith('c') and letras[-2] != ')') or (letras.startswith('a') and letras[1] != '(')):
        return False
    
    return rec(letras[2:-2])


opcoes = ['a(b)c' , 'a(a(b)c)c' , 'a(abc)c' , 'a(a(a(a)c)c)c' , 'a(aacc)c']


for string in opcoes:
    if rec(string):
        print(f"{string} pertence a W")
    else:
        print(f"{string} não pertence a W")
