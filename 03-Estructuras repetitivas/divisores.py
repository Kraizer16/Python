# Mostrar los divisores de un número ingresado por el ususario 

n = int(input("Ingrese un número entero positivo: "))

if n > 1:
    for d in range (1, n):
     if n % d == 0:
         print(d, end=", ")
         
else:
    print("ERROR. El número debe ser mayor que 1")