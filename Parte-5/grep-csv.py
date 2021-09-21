#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import csv
import sys

# zona de funciones
def imprime_csv(lista):
	""" Imprime en la salida estándar la lista en formato CSV """
	writer_csv = csv.writer(sys.stdout)  # el archivo de salida relacionado con la pantalla
	writer_csv.writerows(lista)

def get_datos_csv(archivo):
	""" Lee todas las filas de archivo y regresa la lista """
	with open(archivo) as lector_txt:
		reader_csv = csv.reader(lector_txt)
		filas = list( reader_csv )

	return filas

@click.command()
@click.option("-n", default=-1, help="Indica la columna a realizar la búsqueda")
@click.argument("archivo")
@click.argument("texto", default="")
def main(n, archivo, texto):
	"""
	Imprime todas las líneas de ARCHIVOS en formato CSV
	"""
	lista = get_datos_csv(archivo)
	lista_filtrada = []
	for linea in lista:
		# linea -> ["0", "Hulk", "..."] -> " ".join(linea) -> "0 Hulk Male ..."
		if n >= 0:  # se busca texto por columna N
			if texto in linea[n]:
				lista_filtrada.append(linea)
		else:  # se busca texto en todas las columnas
			if texto in " ".join(linea):
				lista_filtrada.append(linea)

	imprime_csv(lista_filtrada)

# Condición para que el main() sólo se ejecute como script
if __name__ == '__main__':
	main()






