n = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(2, n + 1, 2):
    suma += i
print("La suma de los pares hasta", n, "es", suma)
