def rec(letras):
    if letras == 'a' or letras == 'b':
        return True
    
    if letras.endswith('a') and letras[-2] != 'a':
        return False
    
    return rec(letras[:-1]) and letras[-1] == 'b'


opcoes = ['a', 'ab', 'aba', 'aaab', 'bbbbb']


for letra in opcoes:
    if rec(letra):
        print(f"{letra} pertence a S")
    else:
        print(f"{letra} não pertence a S")
