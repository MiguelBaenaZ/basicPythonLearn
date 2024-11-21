# -*- coding: cp1252 -*-

#VARIABLES PRIMARIAS DEL PROGRAMA.

listaN = [] #AQUI SE GUARDAN LOS NUMEROS INGRESADOS

global listaT #listas de rotacion primero se ingresa todos las valores transformados
global listaP

varia = 0 # variables que puede manejar el sistema
 

###########################FUNCIONES################################

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
    
    while len(lista) != varia: 
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
    
    if listaReem[n][0] == 0:     
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
                print "Diferente Final",listad[n]

        n = n + 1        

def comparar(listab,listac,n,listaReem,difer):
    con = 0
    l = 0
    global dife
    dife = difer #igualacion varabiables globales
    while len(listab) > l:
        if listab[l] != listac[l]:
            con = con + 1
        l = l + 1    
        
    if con < 2:
        reemplazador(listab,listac,n,listaReem)

    if con >= 2:
        dife = dife + 1
        return dife       

def analizador (listad,listae,n1,listaReem,tamanodelistaTrabajando):
    n = 0
    soloUnavez = 0
    global difer
    while len(listad) > n:
        m = 0
        difer = 0
        while len(listae) > m:
            comparar(listad[n],listae[m],n1,listaReem,difer) #n1 POSICION DE ESTA LISTA EN LA LISTA P
            difer = dife #igualacion de variables globales


                
            m = m + 1
            if n == 0 and difer == len(listae):
                print "Diferente",listad[n]

            if tamanodelistaTrabajando-2 == n1 and soloUnavez == 0 and len(listae) == m:
                analizadorEspecial(listae,listad)
                soloUnavez = 1
                
        n = n + 1    

            
def recorrer (listaf,listag,n,listaReem,tamanodelistaTrabajando):
    if listaf != [] and listag != []:
        analizador(listaf,listag,n,listaReem,tamanodelistaTrabajando)
        
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
    global solucion
    pro = 0
    while len(listaPro) > pro+1:
        recorrer(listaPro[pro],listaPro[pro+1],pro,listaReem,len(listaPro))
        pro = pro + 1

    listavacia(listaReem)
    imprimir(listaReem)
    
    if len(listaReem) == 1:
        solucion = False
    

def despliegue(listaR1,listaR2):
    while solucion: 
        
        crearlistaP(len(listaR1)-1,listaR2)
        algoritmo(listaR1,listaR2)
        listaR1 = []

        crearlistaP(len(listaR2)-1,listaR1)
        algoritmo(listaR2,listaR1)
        listaR2 = []

    if solucion == False:
        print "SOLUCIONADO"


#def conversionLog(listasolucion):
        
                
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

listaT = []
listaP = []
solucion = True

print "CUANTAS VARIABLES DESEA INGRESAR: "
varia = int(input())

crearlistaP(varia+1,listaP)
print

print "CUANTOS NUMEROS DESEA INGRESAR: "
cant = int(input())
ingresar(cant)
print listaN

#INICIA EL PROCEDIMIENTO
convertir(listaN)

#REVISA SI HAY ELEMENTOS O POSICONES VACIAS
listavacia(listaP)
print
imprimir(listaP)
print
print

#PROCESA LA LISTA DE UNOS Y LLEGA A LA SOLUCION 
despliegue(listaP,listaT)









