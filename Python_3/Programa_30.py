#30
#Alvaro Medel García
#Vamos a crear un programa para trabajar con una pila. Una pila es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el último elemento que se añade al conjunto es el primero que se puede sacar.

#Para representar una pila vamos a utilizar una lista de cadenas de caracteres.

#Vamos a crear varias funciones para trabajar con la pila:
#LongitudPila: Función que recibe una pila y devuelve el número de elementos que tiene.
#EstaVaciaPila: Función que recibe una pila y que devuelve si la pila está vacía, no tiene elementos.
#EstaLlenaPila: Función que recibe una pila y que devuelve si la pila está llena.
#AddPila: función que recibe una cadena de caracteres y una pila, y añade la cadena a la pila, si no está llena. si esta llena muestra un mensaje de error.
#SacarDeLaPila: Función que recibe una pila y devuelve el último elemento añadido y lo borra de la pila. Si la pila está vacía muestra un mensaje de error.
#EscribirPila: Función que recibe una pila y muestra en pantalla los elementos de la pila.

#Realiza un programa principal que nos permita usar las funciones anterior, que nos muestre un menú, con las siguientes opciones:
#Añadir elemento a la pila
#Sacar elemento de la pila
#Longitud de la pila
#Mostrar pila
#Salir
def LongitudPila(pila):
	return len(pila)
def EstaVaciaPila(pila):
	return len(pila) == 0

def AddPila(cad, pila):
	pila.append(cad)
def SacarDeLaPila(pila):
	if not EstaVaciaPila(pila):
		return pila.pop(len(pila)-1)
	else:
		print("No se puede sacar elemento. La pila está vacia")
		return ""
def EscribirPila(pila):
	for elem in pila:
		print(elem,end=" ")
	print()
		
mipila = []
while True:
	print("1.- Añadir elemento a la pila")
	print("2.- Sacar elemento de la pila")
	print("3.- Longitud de la pila")
	print("4.- Mostrar pila")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la pila:")
		AddPila(elem,mipila)
	elif opcion == 2:
		print(SacarDeLaPila(mipila))
	elif opcion == 3:
		print("Longitud: ",LongitudPila(mipila))
	elif opcion == 4:
		EscribirPila(mipila)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
