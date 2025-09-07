ventas = [0] * 7
dias = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

while True:
    print("\n--- CONTROL DE VENTAS ---")
    print("1. Ingresar ventas por día")
    print("2. Mostrar total de ventas")
    print("3. Mostrar promedio semanal")
    print("4. Salir")
    opcion = int(input("Elija opción: "))

    if opcion == 1:
        for i in range(7):
            ventas[i] = float(input(f"Ingrese ventas del {dias[i]}: "))
    elif opcion == 2:
        print("Total ventas de la semana:", sum(ventas))
    elif opcion == 3:
        print("Promedio de ventas semanales:", sum(ventas) / 7)
    elif opcion == 4:
        break
