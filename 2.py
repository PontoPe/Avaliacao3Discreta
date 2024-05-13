def prog_geo(n, a, r):
    if n == 1:
        return a
    else:
        return r * prog_geo(n-1, a, r)
    
# sendo a o termo inicial, r a razao e n o numero de termos