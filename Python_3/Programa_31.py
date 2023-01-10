#31
#Alvaro Medel García
#Vamos a realizar un programa similar al anterior para trabajar con una cola. Una cola es una estructura de datos que nos permite guardar un conjunto de variables. La característica fundamental es que el primer elemento que se añade al conjunto es el primero que se puede sacar.

#En realizada nos sirven todas las funciones del ejercicio anterior 
# menos la función SacarDeLaCola que es la que tienes que modificar.
def LongitudCola(cola):
	return len(cola)
def EstaVaciaCola(cola):
	return len(cola) == 0
def AddCola(cad, cola):
	cola.append(cad)
def SacarDeLaCola(cola):
	if not EstaVaciaCola(cola):
		return cola.pop(0)
	else:
		print("No se puede sacar elemento. La cola está vacia")
		return ""
def EscribirCola(cola):
	for elem in cola:
		print(elem,end=" ")
	print()
micola = []
while True:
	print("1.- Añadir elemento a la cola")
	print("2.- Sacar elemento de la cola")
	print("3.- Longitud de la cola")
	print("4.- Mostrar cola")
	print("5.- Salir")
	opcion = int(input())
	if opcion == 1:
		elem = input("Dame la cadena para añadir a la cola:")
		AddCola(elem,micola)
	elif opcion == 2:
		print(SacarDeLaCola(micola))
	elif opcion == 3:
		print("Longitud: ",LongitudCola(micola))
	elif opcion == 4:
		EscribirCola(micola)
	elif opcion == 5:
		break
	else:
		print("Opción incorrecta")
