#Creo e inicializo las variables
numero = 0
bucle = "si"
while bucle == "si":
	numero = int(input("Introduce el numero que quieras:\n"))
	if (numero % 2 == 0):
		print("este numero es par") 
	if (numero % 2 != 0):
		print("este numero es inpar")
	bucle = input ("Quieres añadir mas datos a la tabla?: si/no ?\n")	
	if bucle != "si":
		break