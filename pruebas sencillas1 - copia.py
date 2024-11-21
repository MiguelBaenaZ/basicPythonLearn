global a

a=[]

def hola(b):
    global a
    a.append(b)
    print a

hola(2)    
