#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zona de funciones
def range_cuadrados(a, b):
	""" Crea la lista de números al cuadrado en el rango de a a b-1 """
	numeros = list( range(a, b) )  # crea una lista
	# Construyendo la lista de números al cuadrado
	cuadrados = []
	for i in numeros:
		cuadrados.append(i ** 2)

	return cuadrados  # regresamos una lista de números al cuadrado

# zona principal
for n in range_cuadrados(10, 21):
	print(n)
