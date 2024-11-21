lista1 =[[0, '-', 0, '-', 1],[0, '-', 0, '-', 1],['-', '-', 0, 0, 1],['-', '-', 0, 0, 1],[0, '-', 0, 1, '-'],[0, '-', 0, 1, '-'],[0, 1, 0, '-', '-'],[0, 1, 0, '-', '-']]
lista2 =[[0, 0, 0, '-', '-'],[0, '-', 0, 0, '-'],[0, 0, 0, '-', '-'],[0, '-', 0, '-', 0],[0, '-', 0, 0, '-'],[0, '-', 0, '-', 0]]

def compararEspecial(listab,listac):
    con = 0
    l = 0
    global difeEspecial
    difeEspecial = diferEspecial
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
    if con >= 2:
        difeEspecial = difeEspecial + 1
        return difeEspecial
def analizadorEspecial(listad,listae):
    n = 0
    global diferEspecial
    while len(listad) > n:
        m = 0
        diferEspecial = 0
        while len(listae) > m:
            compararEspecial(listad[n],listae[m])
            diferEspecial = difeEspecial
            m = m + 1
            if diferEspecial == len(listae):
                print "Diferente Final",listad[n]  # este es el otro caso que funciona bien

        n = n + 1
#analizadorEspecial(lista1,lista2)
        
print 2**5
