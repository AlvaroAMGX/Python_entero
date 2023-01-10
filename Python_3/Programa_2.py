#2
#Realizar un programa que comprueba si una cadena leída por teclado comienza por una subcadena introducida por teclado.
#Alvaro Medel García
# Pedimos al usuario que introduzca la cadena y la subcadena
cadena = input("Introduce una cadena: ")
subcadena = input("Introduce una subcadena: ")
# Comprobamos si la cadena comienza por la subcadena
if cadena.startswith(subcadena):
    # Si es así, mostramos un mensaje de éxito
    print("La cadena comienza por la subcadena especificada")
else:
    # Si no, mostramos un mensaje de error
    print("La cadena no comienza por la subcadena especificada")


