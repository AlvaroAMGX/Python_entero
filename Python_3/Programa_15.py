#15
#Alvaro Medel García
#Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena
#Tenemos un diccionario y una frase donde vamos a introducir una frase y ver cuantas veces aparece una cadena.
dict = {}
frase = input("Frase: ")
lista_palabras=frase.split(" ")
for palabra in lista_palabras:
	if palabra in dict:
		dict[palabra]+=1
	else:
		dict[palabra]=1	
for campo,valor in dict.items():
	print (campo," ha aparece ",valor ," veces")