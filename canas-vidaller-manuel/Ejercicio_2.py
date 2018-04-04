#Creo e inicializo las variables

edad	= 0
nombre	= ""

#Pregunto la edad
edad = int(input("¿Cúal es su edad?:\n"))

#Comprobamos si es mayor o menor de Edad
if edad < 18:
	print ("El programa es sólo para mayores de edad")
else:
	nombre = input ("¿Cómo se llama?:\n")
	print ("Me alegro de conocerle", nombre)

#Siempre nos despedimos
print ("Hasta Pronto")
