# -*- coding: cp1252 -*-



listaN = []

listaT = []
listaP = []

varia = 0

solucion  = True

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
    
    while len(lista) != varia: #cambiar para tener mas de 5 variables
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


def agreLista3D(listaz,n,listaReem):
    print "n vale: ", n
    
    if listaReem[n][0] == 0:     #puede haber un error comparar con agrupar
        listaReem[n][0] = listaz
    else:
        listaReem[n].append(listaz)
   
        

def reemplazador(lista1,lista2,n,listaReem):
    j = 0
    listareem = lista2[:]
    while len(listareem) > j:

       if lista1 [j] != listareem[j]:
           listareem[j] = "-" 
           agreLista3D(listareem,n,listaReem)

       j = j + 1


def comparar(listab,listac,n,listaReem):
    con = 0
    l = 0
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
        
    if con < 2:
        print "compatibles"
        reemplazador(listab,listac,n,listaReem)

    if con >= 2:
        return
       
       
def analizador (listad,listae,n1,listaReem): #en el caso lista de lista seria desde el inicio 
    n = 0
    while len(listad) > n:
        m = 0

        while len(listae) > m:
            comparar(listad[n],listae[m],n1,listaReem)#mandar la posicion n
            m = m + 1

        n = n + 1    
            
def recorrer (listaf,listag,n,listaReem):
    if listaf != [] and listag != []:
        analizador(listaf,listag,n,listaReem)
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
                

def algoritmo(listaPro,listaReem):
    pro = 0
    while len(listaPro) > pro+1:
        recorrer(listaPro[pro],listaPro[pro+1],pro,listaReem)
        pro = pro + 1

    listavacia(listaReem)
    imprimir(listaReem)
    if len(listaReem) == 1:
        solucion = False
    

def despliegue(listaR1,listaR2):
    while solucion:
        if listaR2 == []:
            crearlistaP(len(listaR1)-1,listaR2)
            algoritmo(listaR1,listaR2)
            del listaR1
            
        if listaR1 == []:
            print "entro"
            crearlistaP(len(listaR2)-1,listaR1)
            algoritmo(listaR2,listaR1)
            del listaR2
                

def crearlistaP(v,listaCre): #debe crear el tamaño de las listas segun los unos corregir
    v1 = 0
    while v > v1:
        listaCre.append([0])
        v1 = v1 + 1

def listavacia(listava):
    k = 0
    while len(listava) > k:
        if listava[k] == [0]:
            del listava[k]
            listavacia(listava)
            
        k = k + 1

##############MAIN################

print "CUANTAS VARIABLES DESEA INGRESAR: "
varia = int(input())
crearlistaP(varia+1,listaP)
print
print listaP
print listaT
         

print "CUANTOS NUMEROS DESEA INGRESAR: "
cant = int(input())
ingresar(cant)
print listaN
convertir(listaN)
print
imprimir(listaP)
print
print

despliegue(listaP,listaT)







