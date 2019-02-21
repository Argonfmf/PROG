def prastevilo(n):
    '''Preveri, če je število praštevilo.'''
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

def veselo_prastevilo(n):
    '''Naredi tabelo vseh veselih praštevil do 10000.'''
    tab = []
    if prastevilo(n) == True:
        if
    