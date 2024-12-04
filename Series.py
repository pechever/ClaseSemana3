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
    
 #Cesar  Vasconez

# Código Python – Contar Números Pares
def contar_pares(lista):
    contador = 0
    for numero in lista:
        if numero % 2 == 0:
            contador += 1
    return contador
 
# Obtener la lista de números desde el usuario

entrada = input("Ingrese una lista de números separados por espacios: ")
numeros = [int(x) for x in entrada.split()]
 
cantidad_pares = contar_pares(numeros)
print("Cantidad de números pares:", cantidad_pares)
