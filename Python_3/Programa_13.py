#13
#Alvaro Medel García
#Queremos guardar los nombres y la edades de los alumnos de un curso. 
#Realiza un programa que introduzca el nombre y la edad de cada alumno. 
#El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*) Al finalizar se mostrará los siguientes datos:
#Todos lo alumnos mayores de edad.
#Los alumnos mayores (los que tienen más edad)
#Tenemos dos listas y una variable que se llama nombre donde vamos a introducir los nombres de los alumnos con su edad
nombres=[]
edades=[]
nombre=""
while True:
    nombre=input(str("Introduce un nombre del alumno o * para salir: "))
    if nombre != "*":
            nombres.append(nombre)
            edades.append(int(input("Dime la edad: ")))
    if nombre == "*": 
        break

edad_max = max(edades)
print("Alumnos mayores de edad : ")
for nombre,edad in zip(nombres,edades):
	if edad >= 18:
		print(nombre)
	
print("Alumnos mayores :")
for nombre,edad in zip(nombres,edades):
	if edad == edad_max:
		print(nombre)
