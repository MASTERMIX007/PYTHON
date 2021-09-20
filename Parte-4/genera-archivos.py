#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# Zona de funciones
def obtiene_numero():
	""" Obtiene un número desde la línea de comandos """
	argumentos = sys.argv[1:]
	numero_str = argumentos[0]

	if numero_str.isdigit():
		numero = int(numero_str)
	else:
		numero = None  # Nulo

	return numero

# Zona principal
numero = obtiene_numero()
if numero != None:
	if numero < 0:
		print("Error: el número tiene que ser mayor a cero!")
	else:
		for nom in archivos_gen(numero):
			print(nom)
else:
	print("Error: el argumento no es un entero válido!")

