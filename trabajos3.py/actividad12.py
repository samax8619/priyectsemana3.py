n = int(input("Ingrese un número entero: "))
es_primo = True
if n <= 1:
    es_primo = False
else:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break
print("Es primo" if es_primo else "No es primo")
