# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    

"""
Marcos Joel Plata Barahona
"""
def numeros_primos():
    n = int(input("Ingresa un numero: "))
    for i in range(n + 1):
        if(i % 2 == 0):
            print(f"{i} es primo")

numeros_primos()