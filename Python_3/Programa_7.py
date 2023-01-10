#7
#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la aparición del primer carácter en la cadena por el segundo carácter.
#Alvaro Medel García
#Con estas variables escribiremos una frase y con los caracteres los intercambiaremos.
cadena=input("Dime una frase: ")
caracter1=input("Introduce el caracter que quieres cambiar :")
caracter2=input("Introduce el caracter que quieres introducir :")
print(str.replace(cadena,caracter1,caracter2))