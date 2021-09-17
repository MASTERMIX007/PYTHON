#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

# 1. Leer dirección ip4 desde la línea de comandos
# 2. Descomponer la dirección en octetos
# 3. Contar el número de octetos, si es distinto a 4 entonces
#    la ip es inválida
# 4. Para cada octeto validar si está en el rango 0 a 255, si
#    alguno no lo está entonces la ip es inválida
# 5. Imprimir si la dirección es válida o inválida


ip = sys.argv[1]  # 1.
octetos = ip.split(".")  # 2.
valida = True  # postura, se asume que la ip es válida

# comparar si no hay 4 octetos entonces valida = False
if len(octetos) != 4:
	valida = False
# comparar si el 1er octeto no esta en el rango 0-255 entonces valida = False
elif int(octetos[0]) > 255 or int(octetos[0]) < 0:
	valida = False
# comparar si el 2er octeto no esta en el rango 0-255 entonces valida = False
elif int(octetos[1]) > 255 or int(octetos[1]) < 0:
	valida = False
# comparar si el 3er octeto no esta en el rango 0-255 entonces valida = False
elif int(octetos[2]) > 255 or int(octetos[2]) < 0:
	valida = False
# comparar si el 4er octeto no esta en el rango 0-255 entonces valida = False
elif int(octetos[3]) > 255 or int(octetos[3]) < 0:
	valida = False
# comparar si valida = True entonces imprimir mensaje de Válida, en caso
# contrario imprimir Inválida.
if valida:
	print("Válida")
else:
	print("Inválida")
