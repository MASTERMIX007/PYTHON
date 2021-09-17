#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Solicitar un número entero al usuario mayor que cero
# 2. Si el usuario proporciona un valor que no esté en el rango que imprima un mensaje de error
# 3. Si el usuario proporciona un valor que no sea entero que imprima un mensaje de error
# 4. Crear una lista con los números enteros desde el 1 hasta el proporcionado por el usuario
# 5. Imprimir la lista de números en la salida estándar

# Tu código aquí!
n_str = input("Dame un entero mayor a cero: ")
if not n_str.isdigit():
	print("Error: el valor no es un entero!")
else:
	n = int(n_str)
	if n <= 0:
		print("Error: el número tiene que ser mayor a cero!")
	else:
		# si llegamos aquí es que no hay errores y podemos crear la lista
		print("Generando lista de numeros ...")
		numeros_lst = range(1, n+1)
		# print("Creando lista de raices ...")
		# raices_lst = []
		# for i in numeros_lst:
		# 	raices_lst.append( i ** (1/2) )

		for i in numeros_lst:
			print(i)









