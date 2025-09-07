hora = int(input("Ingrese la hora actual (0-23): "))
presencia = input("¿Hay alguien en casa? (si/no): ").lower()

if 18 <= hora or hora < 6:
    if presencia == "si":
        print("Es de noche y hay alguien en casa. Luces encendidas.")
    else:
        print("Es de noche pero no hay nadie en casa. Luces apagadas.")
else:
    print("Es de día. Luces apagadas.")
