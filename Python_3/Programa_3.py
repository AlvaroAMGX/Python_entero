#3
#Alvaro Medel García
#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas veces aparece el carácter en la cadena.
#Hay dos variables una cadena y una subcadena con la que voy a contar cuantas veces aparece esa subcadena.
cadena=input("Dame una frase: ")
caracter=input("Dime un caracter que quieres buscar: ")
if len(caracter)==1:
    print('Tu aparace ',cadena.count(caracter) ," veces en la frase")
else:
    print("El caracter es demasiado largo")