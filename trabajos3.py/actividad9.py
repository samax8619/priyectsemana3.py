temps = input("Ingrese temperaturas en °C separadas por coma: ")
celsius = [float(t) for t in temps.split(",")]
for t in celsius:
    fahrenheit = (t * 9/5) + 32
    print(f"{t} °C = {fahrenheit:.2f} °F")
