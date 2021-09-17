#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Leer un número desde la línea de comandos (sys.argv)
# 2. Si el número es un entero continuar (if)
# 2.1    Si el número < 256 continuar (if)
# 3.         Multiplicar por 10 (operación)
# 3.1    Si el número no es menor a 256 (else)
# 3.2        Imprime mensaje de error. (print)
# 4. Si el número no es un entero (else)
# 5.     Imprime mensaje de error. (print)
# 6. Imprimir el resultado. (print)

import sys

argumentos = sys.argv[1:]
numero_str = argumentos[0]  # "10", "115", "0", "uno", "10.5"
if numero_str.isdigit():
	numero = int(numero_str)
	if numero < 256:
		numero = numero * 10
	else:
		print("Error: el número no puede ser mayor a 255")
else:
	print("Error: lo que has escrito no es un número entero!")
	numero = 0

print(numero)

