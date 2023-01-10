#10
#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual adelante que atrás.
#Con las dos variables veremos si la cadena es igual escrita al reves.
cadena=input("Introduce una frase: ")
revcad=cadena[::-1]
if cadena == revcad:
    print("Es palindromo")
else:
    print("No es palindromo")