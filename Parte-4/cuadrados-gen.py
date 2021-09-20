#!/usr/bin/env python
# -*- coding: utf-8 -*-

# zona de funciones
def range_cuadrados(a, b):
	""" Crea la lista de números al cuadrado en el rango de a a b-1 """
	numeros = range(a, b)  # usamos un generador
	for i in numeros:
		yield i ** 2  # regresando un sólo valor

# zona principal
for n in range_cuadrados(10, 2100_000_000):  # usando generador -> 0, 1, 2, ...
	print(n)
