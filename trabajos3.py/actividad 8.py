palabra = input("Ingrese una palabra: ").lower()
if palabra == palabra[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
