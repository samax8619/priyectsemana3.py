import random
import time

humedad = float(input("Ingrese la humedad actual del suelo (0-100): "))
umbral = float(input("Ingrese el umbral deseado de humedad (0-100): "))

while True:
    if humedad < umbral:
        print(f"Humedad: {humedad:.2f}% - Activando riego...")
        time.sleep(2)
        humedad += random.uniform(5, 15)
    else:
        print(f"Humedad: {humedad:.2f}% - Humedad adecuada, sin riego.")
        break
    time.sleep(1)
