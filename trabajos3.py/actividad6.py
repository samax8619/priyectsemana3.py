n = int(input("Ingrese un número entero no negativo: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("El factorial de", n, "es", factorial)
