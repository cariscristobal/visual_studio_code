edad = int(input("Introduce tu edad por favor: "))

while edad <= 0:
    print("Has introducido una edad no valida. Vuelve a intentarlo")
    edad = int(input("Introduce tu edad por favor: "))

print("Gracias por colaborar. Puedes pasar")
print("Edad del aspirante "+ str(edad))