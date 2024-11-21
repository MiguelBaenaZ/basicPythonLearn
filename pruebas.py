print "INGRESE 10 VARIABLES"
a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())
#e = int(input())
#f = int(input())
#g = int(input())
#h = int(input())
#i = int(input())
#j = int(input())

num = a
lista = []
reco = 0

while num >= 1:
    lista.insert(0,num%2)
    num = num // 2
    reco = reco + 1

while len(lista) != 5:
    lista.insert(0,0)
        
print len(lista)    
resultado = "".join(str(i) for i in lista)
print (resultado)
