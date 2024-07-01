"""
Marcos Joel Plata Barahona
"""
def numeros_primos():
    n = int(input("Ingresa un numero: "))
    for i in range(n + 1):
        if(i % 2 == 0):
            print(f"{i} es primo")

numeros_primos()