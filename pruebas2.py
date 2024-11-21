# -*- coding: cp1252 -*-

listaN = []

listaunos0 = []
listaunos1 = []
listaunos2 = []
listaunos3 = []
listaunos4 = []
listaunos5 = []

listaT = []

def implisunos():

    if listaunos0 != []:
        print listaunos0

    if listaunos1 != []:
        print listaunos1

    if listaunos2 != []:
        print listaunos2    

    if listaunos3 != []:
        print listaunos3
    
    if listaunos4 != []:
        print listaunos4
    
    if listaunos5 != []:
        print listaunos5

        
def agrupar(listaa):
    if listaa.count(1) == 0:
        listaunos0.append(listaa)

    if listaa.count(1) == 1:
        listaunos1.append(listaa)

    if listaa.count(1) == 2:
        listaunos2.append(listaa)   

    if listaa.count(1) == 3:
        listaunos3.append(listaa)
   
    if listaa.count(1) == 4:
        listaunos4.append(listaa)    
    
    if listaa.count(1) == 5:
        listaunos5.append(listaa)

def contador(listah):
    contad = listah.count(1)

    return contad

        

def binario(num):
    lista = []
    
    while num >= 1:
        lista.insert(0,num%2)
        num = num // 2
    
    while len(lista) != 5:
        lista.insert(0,0)

    agrupar(lista)
    lista = []


def comparar(listab,listac):
    con = 0
    l = 0
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
        
    if con < 2:
        print "compatibles"
        v = listab.count(1)
        reemplazador(listab,listac,listaT,v)

    if con >= 2:
        return
        

def ingresar(cant):
    i = 1
    while cant >= i:
        print "INGRESE LA VARIABLE NUMERO ",i," :"
        numero = int(input())
        listaN.append(numero)
        i = i + 1


def convertir(lista):
    for r in lista:
        binario(r)

def reemplazador(lista1,lista2,listatransi,v):
    j = 0
    while len(lista2) > j:

       if lista1 [j] != lista2[j]:
           lista2[j] = "-"
           #listatransi.append(lista2)
           listatransi[v] = lista2

       j = j + 1
       
def analizador (listad,listae):
    n = 0
    while len(listad) > n:
        m = 0

        while len(listae) > m:
            comparar(listad[n],listae[m])
            m = m + 1

        n = n + 1    
            
def estado (listaf,listag):
    if listaf != [] and listag != []:
        analizador(listaf,listag)
    else:
        return
        
    

    

        
#print "\n binario "
# print len(lista) permite saber el tamaño de una lista
#print lista
#resultado = "".join(str(i) for i in lista)
#print (resultado)

#print "\n comparacion"
#comparar(lista,lista1)

#print "\n agrupacion"
#agrupar(lista)
#agrupar(lista1)


print "CUANTOS NUMEROS DESEA INGRESAR: "
cant = int(input())
ingresar(cant)

print listaN

convertir(listaN)
implisunos()

estado(listaunos1,listaunos2)

print "\n lista de transicion \n"
print listaT


