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
		print("Error: el número no es un octeto!")
	elif numero > 255:
		print("Error: el número no es un octeto!")
	else:
		print(f"El número {numero} es un octeto!")
else:
	print("Error: el argumento no es un entero válido!")

