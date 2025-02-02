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
    
#Alfonso Eduardo Vega Cañarejo 

p = 45
q = 15
producto = p * q
print(f"El producto de {p} y {q} es {producto}")
print("-----------------------------------")
<<<<<<< HEAD
=======

>>>>>>> 495a68a6dbde6952db5ef0507a5354ef6a2cc6ff
