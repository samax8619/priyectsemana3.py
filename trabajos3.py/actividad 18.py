import random
humedad = int(input("Ingrese la humedad actual del suelo: "))
umbral = int(input("Ingrese el umbral deseado de humedad: "))

while humedad < umbral:
    print(f"Humedad {humedad}% -> Activando riego...")
    humedad += random.randint(5, 15)

print(f"Humedad alcanzada: {humedad}% -> Riego detenido")
