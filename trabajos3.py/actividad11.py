n = int(input("Ingrese un número entero positivo: "))
contador = 0
while n > 0:
    contador += 1
    n //= 10
print("Cantidad de dígitos:", contador)
