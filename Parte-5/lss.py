#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import os
import time

# zona de funciones
def imprime_tabla(lista):
	""" Imprime la lista en forma de tabla """
	for a_lst in lista:
		# a_lst -> ["nombre", 12345, "fecha"]
		print( f"{a_lst[1]:10}  {a_lst[2]:10}  {a_lst[0]}" )

def get_archivos(carpeta, sort, reverse, sort_size):
	""" Obtiene la lista de archivos de la carpeta y sus atributos """
	try:
		archivos = os.listdir(carpeta)
	except FileNotFoundError:
		return None

	# la variable archivos tiene que existir con una lista, aunque sea vacia
	lista = []
	for arch in archivos:
		arch = os.path.join(carpeta, arch)  # /home/kmmx, .mozilla -> /home/kmmx/.mozilla
		tam = os.path.getsize(arch)
		fecha_ms = os.path.getmtime(arch)
		fecha_obj = time.localtime(fecha_ms)
		fecha = time.strftime("%d-%m-%Y", fecha_obj)
		arch_lst = [arch, tam, fecha]
				#    0     1     2
		lista.append(arch_lst)

	if sort:
		lista.sort()
	if sort_size:
		lista.sort(key=lambda v: v[1])  # ordenamos en base al tamaño
	if reverse:
		lista.reverse()

	return lista

@click.command()
@click.option("--sort", is_flag=True, help="Imprime la lista ordenada")
@click.option("--reverse", is_flag=True, help="Imprime la lista ordenada descendentemente")
@click.option("--sort-size", is_flag=True, help="Imprime la lista ordenada por tamaño")
@click.argument("carpeta", default=".")
def main(sort, reverse, sort_size, carpeta):
	"""
	Imprime la lista de archivos de CARPETA en la salida estándar
	"""
	lista = get_archivos(carpeta, sort, reverse, sort_size)
	if lista == None:
		print(f"Error: la carpeta {carpeta} no existe!")
	else:
		imprime_tabla(lista)

# Condición para que el main() sólo se ejecute como script
if __name__ == '__main__':
	main()






