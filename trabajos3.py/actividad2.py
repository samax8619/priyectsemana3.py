aprobados = 0
reprobados = 0
suma_notas = 0
total_estudiantes = 0

while True:
    for i in range(1, 4):
        nombre = input(f"Nombre del estudiante {i}: ")
        p1 = float(input("Nota p1: "))
        p2 = float(input("Nota p2: "))
        p3 = float(input("Nota p3: "))
        definitiva = (p1 + p2 + p3) / 3
        print(f"Nota final de {nombre}: {definitiva:.2f}")

        if definitiva >= 3.0:
            aprobados += 1
        else:
            reprobados += 1
        suma_notas += definitiva
        total_estudiantes += 1

    continuar = input("¿Desea continuar? (si/no): ")
    if continuar.lower() != "si":
        break

promedio = suma_notas / total_estudiantes
print("\nResumen:")
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio general:", round(promedio, 2))
