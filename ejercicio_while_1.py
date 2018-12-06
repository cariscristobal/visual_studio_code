"""Ejercicio 1:
• Crea un programa que pida números infinitamente. Los números introducidos deben
ser cada vez mayores El programa finalizará cuando se introduce un número menor que
el anterior."""
num1 = int(input("Introduce un número por favor: "))
num2 = int(input("Introduce un número mayor que : " + str(num1) + "\n"))

while num2 > num1:
        num1 = num2
        num2 = int(input("Escriba un numero mayor que: " + str(num1)+ "\n"))

if num2 == num1:
    print("el número ingresado es igual al : " + str(num1))
else:
    print("el número ingresado es menor al " + str(num1))