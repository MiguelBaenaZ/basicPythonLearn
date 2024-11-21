# -*- coding: cp1252 -*-

listaN = []

listaunos0 = []
listaunos1 = []
listaunos2 = []
listaunos3 = []
listaunos4 = []
listaunos5 = []

listaT = [[0],[0],[0],[0],[0]]

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


def binario(num):
    lista = []
    
    while num >= 1:
        lista.insert(0,num%2)
        num = num // 2
    
    while len(lista) != 5:
        lista.insert(0,0)

    agrupar(lista)
    lista = []
        

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


def comparar(listab,listac):
    con = 0
    l = 0
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
        
    if con < 2:
        print "compatibles"
        reemplazador(listab,listac)

    if con >= 2:
        return
       
       
def analizador (listad,listae):
    n = 0
    while len(listad) > n:
        m = 0

        while len(listae) > m:
            comparar(listad[n],listae[m])
            m = m + 1

        n = n + 1    
            
def recorrer (listaf,listag):
    if listaf != [] and listag != []:
        analizador(listaf,listag)
    else:
        return


def imprimirmatriz(listax):

    for i in listax:
        for j in i:
            print j,
        print    


print "CUANTOS NUMEROS DESEA INGRESAR: "
cant = int(input())
ingresar(cant)

print listaN

convertir(listaN)
implisunos()

recorrer(listaunos0,listaunos1)
recorrer(listaunos1,listaunos2)
recorrer(listaunos2,listaunos3)
recorrer(listaunos3,listaunos4)
recorrer(listaunos4,listaunos5)

print "\n lista de transicion \n"
imprimirmatriz(listaT)




