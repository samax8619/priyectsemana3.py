import random
import time

actual = float(input("Ingrese la temperatura actual: "))
deseada = float(input("Ingrese la temperatura deseada: "))

while abs(actual - deseada) > 0.5:
    if actual > deseada:
        print(f"Temperatura actual: {actual:.2f}°C - Aire acondicionado activado")
        actual -= random.uniform(0.3, 1.0)
    elif actual < deseada:
        print(f"Temperatura actual: {actual:.2f}°C - Calefacción activada")
        actual += random.uniform(0.3, 1.0)
    time.sleep(1)

print(f"Temperatura final: {actual:.2f}°C - Dentro del rango aceptable")
