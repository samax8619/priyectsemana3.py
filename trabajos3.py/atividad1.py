import math

while True:
    print("\n--- MENÚ ---")
    print("1. Área y perímetro de un Triángulo")
    print("2. Área y perímetro de un Cuadrado")
    print("3. Área y perímetro de una Circunferencia")
    print("4. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        base = float(input("Base del triángulo: "))
        altura = float(input("Altura del triángulo: "))
        lado1 = float(input("Lado1: "))
        lado2 = float(input("Lado2: "))
        area = (base * altura) / 2
        perimetro = base + lado1 + lado2
        print(f"Área = {area}, Perímetro = {perimetro}")
    elif opcion == 2:
        lado = float(input("Lado del cuadrado: "))
        area = lado ** 2
        perimetro = 4 * lado
        print(f"Área = {area}, Perímetro = {perimetro}")
    elif opcion == 3:
        radio = float(input("Radio de la circunferencia: "))
        area = math.pi * radio ** 2
        perimetro = 2 * math.pi * radio
        print(f"Área = {area}, Perímetro = {perimetro}")
    elif opcion == 4:
        break
