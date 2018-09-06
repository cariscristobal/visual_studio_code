my_string = "Hola Mundo!"
print(my_string)

curso = "Python 3"
nombre = "Cristóbal Caris"

mensaje_final1 = "Nuevo curso de "+ curso + " por " + nombre #1
mensaje_final2 = "Nuevo curso de %s por %s" %(curso,nombre) #2
mensaje_final3 = "Nuevo curso de {} por {}".format(curso, nombre) #3
print(mensaje_final1)
print(mensaje_final2)
print(mensaje_final3)

frase_uno = "Paralelepipedo es un trabalenguas"
print(frase_uno[0:10]) #para recorrer desde la posicion inicial hasta la decima posición
print(frase_uno[0]) # imprime solo la primera posición del string
print(frase_uno[-1]) # Imprime la primera letra desde el final del string
print(frase_uno[-11:-1]) # Imprime desde derecha a izquierda los 10 primeros caracteres
print(frase_uno[0:10:2]) # Imprime los 9 primeros caracteres pero de dos en dos
print(frase_uno[::-1]) # Con esto imprimo la cadena a la inversa