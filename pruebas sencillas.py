lista = [[0,0,0,0,1],[1,2,3,4,7],[1,2,3,4,7],[1,2,3,4,7],[1,2,3,4,7]]
lista2 = [[0,0,1,1,1],[1,2,3,4,7],[1,2,3,4,7],[1,2,3,4,7],[1,2,3,4,7]]
listatransi = []
listaT = [[0],[0],[0],[0],[0]]
listaP = [[0],[0],[0],[0],[0],[0]]
lista3D = []
listaBi = [0,0,0,0,'-']

#lista.append(lista3) 

#print lista[2][2]
#print lista
#print lista2

def compara(listab,listac):
    con = 0
    if listab[0] != listac[0]:
        con = con + 1

    if listab[1] != listac[1]:
        con = con + 1
        
    if listab[2] != listac[2]:
        con = con + 1
        
    if listab[3] != listac[3]:
        con = con + 1

    if listab[4] != listac[4]:
        con = con + 1

    if con < 2:
        print "compatibles"

    if con >= 2:
        print "incompatibles"

#comparar(lista[2],lista3[3])

#lista = []

#print lista

def comparacion(lista,lista2,listatransi):
    j = 0
    while 5 > j:

       if lista [j] != lista2[j]:
           print "mezcla",j+1
           lista2[j] = "-"
           listatransi.append(lista2)

       j = j + 1

def agreLista3D(listaz):
    h = 0
    while len(listaz) > h:
        if listaz.count(0) == len(listaz) - h:
            if listaT[h][len(listaT[h])-1] == 0:
                listaT[h][len(listaT[h])-1] = listaz
            else:
                listaT[h].append(listaz)
            
        h = h + 1

def reemplazador(lista1,lista2):
    j = 0
    listareem = lista2[:]
    while len(listareem) > j:

       if lista1 [j] != listareem[j]:
           listareem[j] = "-" 
           agreLista3D(listareem)

       j = j + 1

def agrupar(listaa):
    p = 0
    while len(listaa) > p:
        if listaa.count(0) == p:
            if listaP[p] == 0:
                listaP[p]=listaa
            else:
                listaP[p].append(listaa)

        p = p + 1

def imprimir(lista):
    r = 0
    while len(lista) > r:
        r1 = 0
        while len(lista[r]) > r1:
            print lista[r][r1]
            r1 = r1 + 1
        print
        print
        r = r + 1

def crearlistaP(v,listaCre):
    lis = [0]
    for i in range(v):
        listaCre.append(lis)

def comparar(listab,listac):
    con = 0
    l = 0
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
    if con >= 2:
        print "diferentes"
        


def analizador(listad,listae):
    n = 0
    while len(listad) > n:
        m = 0
        while len(listae) > m:
            comparar(listad[n],listae[m])
            m = m + 1
        n = n + 1  

def analizador1(listad,listae):
    n = 0
    while len(listad) > n:
        m = 0
        while len(listae) > m:
            con = 0
            l = 0
            while len(listad) > l:
                if listad[m][l] != listae[n][l]:
                    con = con + 1
                    l = l + 1    
                if con >= 2:
                    print "diferentes"
            m = m + 1
        n = n + 1


 
        
        
#comparacion(lista[0],lista2[0],listatransi)

#print listatransi

lista3D.append(lista)
lista3D.append(lista2)

#print lista3D

#print len(lista3D[0])
#print len(lista3D)

#agreLista3D(listaBi)
#reemplazador(lista[0],lista2[0])
#print listaT
#print listaT[1][0]
#print lista2[0]

#agrupar(listaBi)


#imprimir(lista3D)

analizador(lista,lista2)

