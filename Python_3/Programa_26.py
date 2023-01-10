#26
#Alvaro Medel García
#Escribir dos funciones que permitan calcular:
#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas,minutos y segundos o salir del programa.
def Convertir_A_Segundos(h,m,s):
	return h * 3600 + m * 60 + s
def Convertir_A_HMS(seg):
	h = seg//3600
	seg = seg - h*3600
	m = seg//60
	seg = seg - m*60
	s = seg
	return h,m,s
while True:
	print("1.- Convertir a segundos")
	print("2.- Convertir a horas, minutos y segundos")
	print("3.- Salir")
	opcion = int(input())
	if opcion == 1:
		hor = int(input("Horas:"))
		minu = int(input("Minutos:"))
		seg = int(input("Segundos:"))
		print("Corresponde a",Convertir_A_Segundos(hor,minu,seg),"segundos.")
	elif opcion == 2:
		segund=int(input("Segundos:"))
		hor,minu,seg = Convertir_A_HMS(segund)
		print("Corresponde a ",hor,":",minu,":",seg)
	elif opcion == 3:
		break
	else:
		print("Opción incorrecta")

