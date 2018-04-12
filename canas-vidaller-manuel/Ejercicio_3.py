#Creo e inicializo las variables
x = 1
y = 1
z = 1
#Pregunto tres números
while x > 0:
	x = int(input("Dime un número mayor que 0:\n"))
	while x > 0:
		y = int(input ("Dime ahora un número mayor que el anterior:\n"))
		while y > x:
			z = int(input ("Dime ahora otro número pero que sea menor que 0:\n"))
			while z < 0:
				#Creo la operacion 
				print(x, " + ", y, " + ", z, "=",x + y + z)
				break			
			else:
				print ("Error")
		else:	
			print ("Error")
	else:
		#Cambiamos la variable a 1 para que el bucle se pueda ejecutar (línea 8)
		print ("Error")
		x = 1

