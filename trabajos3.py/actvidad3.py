n = int(input("Ingrese un número: "))

# Factorial
factorial = 1
for i in range(1, n + 1):
    factorial *= i

# Pares e impares
pares = 0
impares = 0
suma_pares = 0
suma_impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        pares += 1
        suma_pares += i
    else:
        impares += 1
        suma_impares += i

print(f"Factorial de {n} = {factorial}")
print(f"Cantidad de pares: {pares} | Suma pares = {suma_pares}")
print(f"Cantidad de impares: {impares} | Suma impares = {suma_impares}")
