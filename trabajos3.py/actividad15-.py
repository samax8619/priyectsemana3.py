import random

temp_actual = int(input("Ingrese la temperatura actual: "))
temp_deseada = int(input("Ingrese la temperatura deseada: "))

while abs(temp_actual - temp_deseada) > 1:
    if temp_actual > temp_deseada:
        print(f"Temperatura {temp_actual}° -> Aire acondicionado encendido")
        temp_actual -= random.randint(1, 2)
    elif temp_actual < temp_deseada:
        print(f"Temperatura {temp_actual}° -> Calefacción encendida")
        temp_actual += random.randint(1, 2)

print(f"Temperatura alcanzada: {temp_actual}°")
