#14
#La asociación de viticultores tiene como política fijar un precio inicial al kilo de
#uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se
#realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere
#determinar cuánto recibirá un productor por la uva que entrega en un embarque,
#considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial
#cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se
#rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño
#2. Realice un algoritmo para determinar la ganancia obtenida.
#Alvaro Medel García
#Hay cuatro variables los kilos de uva,el precio de la uva,el tipo`y el tamaño que tambien modificara el precio 
kilo=int(input("Ingresa los kilos de uva:"))
precio=int(input("Ingresa el precio por kilo:"))
tipo=str(input("Dime el tipo de uva A o B:"))
tamano=int(input("Dime el tamaño de la uva:"))

if tipo=="A":
    if tamano == 1:
        precio=precio+0.20
    else:
        precio=precio+0.30
else:
    if tamano == 1:
        precio=precio-0.30
    else:
        precio=precio-0.50
total=precio*kilo
print("La ganancia por ",kilo ," kilos de uva es: $",'{:.2f}'.format(total))