print "INGRESE 10 VARIABLES"
a = int(input())
b = int(input())
#c = int(input())
#d = int(input())
#e = int(input())
#f = int(input())
#g = int(input())
#h = int(input())
#i = int(input())
#j = int(input())



lista = []
lista1 = []


listaunos1 = []
listaunos2 = []
listaunos3 = []
listaunos4 = []
listaunos5 = []


def binario(num,lista):
    while num >= 1:
        lista.insert(0,num%2)
        num = num // 2
    
    while len(lista) != 5:
        lista.insert(0,0)

    return lista


def comparar(listab,listac):
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

        
def agrupar(listaa):
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
    
binario(a,lista)
binario(b,lista1)
print "\n binario 1"
print len(lista)
print lista
resultado = "".join(str(i) for i in lista)
print (resultado)

print "\n binario 2"
print len(lista1)
print lista1
resultado1 = "".join(str(i) for i in lista1)
print (resultado1)

print "\n comparacion"
comparar(lista,lista1)

print "\n agrupacion"
agrupar(lista)
agrupar(lista1)
print listaunos1
print listaunos2
print listaunos3
print listaunos4
print listaunos5


