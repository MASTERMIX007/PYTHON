#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time

# zona de funciones
def imprime_tabla(lista):
	""" Imprime la lista en forma de tabla """
	for a_lst in lista:
		# a_lst -> ["nombre", 12345, "fecha"]
		print( f"{a_lst[1]:10}  {a_lst[2]:10}  {a_lst[0]}" )

def lee_valor():
	""" Leer el valor de la carpeta desde la línea de comandos """
	if len(sys.argv) == 1:
		carpeta = "."  # carpeta por default
	else:
		carpeta = sys.argv[1]

	return carpeta

def get_archivos(carpeta):
	""" Obtiene la lista de archivos de la carpeta y sus atributos """
	archivos = os.listdir(carpeta)
	lista = []
	for arch in archivos:
		arch = os.path.join(carpeta, arch)  # /home/kmmx, .mozilla -> /home/kmmx/.mozilla
		tam = os.path.getsize(arch)
		fecha_ms = os.path.getmtime(arch)
		fecha_obj = time.localtime(fecha_ms)
		fecha = time.strftime("%d-%m-%Y", fecha_obj)
		arch_lst = [arch, tam, fecha]
		lista.append(arch_lst)

	return lista

# zona principal
carpeta = lee_valor()
lista = get_archivos(carpeta)
imprime_tabla(lista)








