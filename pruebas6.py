# -*- coding: cp1252 -*-

listaN = []

listaT = [[0],[0],[0],[0],[0]]
listaP = [[0],[0],[0],[0],[0],[0]]

def agrupar(listaa):
    p = 0
    while len(listaa) >= p:
        if listaa.count(1) == p:
            if listaP[p][0] == 0:
                listaP[p][0]=listaa
            else:
                listaP[p].append(listaa)

        p = p + 1 
                
            
def binario(num):
    lista = []
    
    while num >= 1:
        lista.insert(0,num%2)
        num = num // 2
    
    while len(lista) != 5: #cambiar para tener mas de 5 variables
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


def agreLista3D(listaz,n):
    print "n vale: ", n
    
    if listaT[n][0] == 0:     #puede haber un error comparar con agrupar
        listaT[n][0] = listaz
    else:
        listaT[n].append(listaz)
   
        

def reemplazador(lista1,lista2,n):
    j = 0
    listareem = lista2[:]
    while len(listareem) > j:

       if lista1 [j] != listareem[j]:
           listareem[j] = "-" 
           agreLista3D(listareem,n)

       j = j + 1


def comparar(listab,listac,n):
    con = 0
    l = 0
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
        
    if con < 2:
        print "compatibles"
        reemplazador(listab,listac,n)

    if con >= 2:
        return
       
       
def analizador (listad,listae,n1): #en el caso lista de lista seria desde el inicio 
    n = 0
    while len(listad) > n:
        m = 0

        while len(listae) > m:
            comparar(listad[n],listae[m],n1)#mandar la posicion n
            m = m + 1

        n = n + 1    
            
def recorrer (listaf,listag,n):
    if listaf != [] and listag != []:
        analizador(listaf,listag,n)
    else:
        return


def imprimir(lista):
    r = 0
    while len(lista) > r:
        r1 = 0
        while len(lista[r]) > r1:
            print lista[r][r1]
            r1 = r1 + 1
        print
        r = r + 1  
                

def algoritmo(listaPro):
    pro = 0
    while len(listaPro) > pro+1:
        recorrer(listaPro[pro],listaPro[pro+1],pro)
        pro = pro + 1         
         

print "CUANTOS NUMEROS DESEA INGRESAR: "
cant = int(input())
ingresar(cant)
print listaN

convertir(listaN)

imprimir(listaP)

algoritmo(listaP)

print
print "lista de transicion \n"

imprimir(listaT)




