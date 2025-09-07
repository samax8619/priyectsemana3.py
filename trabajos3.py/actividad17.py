hora = int(input("Ingrese la hora actual (0-23): "))
en_casa = input("¿Hay alguien en casa? (si/no): ").lower() == "si"

if 18 <= hora <= 23 or 0 <= hora < 6:  # noche
    if en_casa:
        print("Luces encendidas")
    else:
        print("Luces apagadas")
else:
    print("Es de día, luces apagadas")
