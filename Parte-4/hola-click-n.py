#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hola-click.py

import click


@click.command()
@click.option("-n", default=1, help="Indica el número de veces a imprimir el mensaje")
@click.argument("nombre")  # nombre = sys.argv[1]
def main(n, nombre):
	"""
	Imprime un saludos en la salida estándar usando NOMBRE como parte
	del saludo.
	"""
	for i in range(n):
		print(f"Hola {nombre} saludos desde Click!")


main()