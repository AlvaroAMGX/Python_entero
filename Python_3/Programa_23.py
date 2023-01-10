#23
#Alvaro Medel García
#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y 
#una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” 
#y la contraseña es “asdasd”. 
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
#Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
def Login(nombre,password,intentos):
	intentos += 1
	if nombre == "usuario1" and password == "asdasd":
		return(True,intentos)
	else:
		return(False,intentos)
cuantasveces = 0
while True:
	usuario = input("Usuario:")
	clave = input("Password:")
	entrar,cuantasveces = Login(usuario,clave,cuantasveces)
	if not entrar:
		print("Error. Nombre de usuario o contraseña incorrecta.")
	if entrar or cuantasveces == 3: 
		break
if entrar:
	print("Bienvenidos al sistema")
else: 
	print("No has entrado en el sistema")
