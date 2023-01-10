#9
#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
#Álvaro Medel García
#Son dos variables una para introducir la cadena y la subcadena ver si la contiene.
cadena=input("Introduce una frase: ")
subcadena=input("Introduce una subcadena para saber si la contiene: ")
if subcadena in cadena:
    print("Contiene esa subcadena")
else:
    print("No contiene esa subcadena")