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
# Suma David Guzman
suma = 2 + 3
print(suma)

# Resta
resta = 5 - 2
print(resta)

# Multiplicación
multiplicacion = 3 * 4
print(multiplicacion)

# División
division = 10 / 2
print(division)
