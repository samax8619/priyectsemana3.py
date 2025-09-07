n = int(input("Ingrese un número entero positivo: "))
numeros = list(range(1, n + 1))
pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]
print("Pares:", pares)
print("Impares:", impares)
