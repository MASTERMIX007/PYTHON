#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hola-click.py

import click


@click.command()
@click.argument("nombre")  # nombre = sys.argv[1]
def main(nombre):
	"""
	Imprime un saludos en la salida estándar usando NOMBRE como parte
	del saludo.
	"""
	print(f"Hola {nombre} saludos desde Click!")


main()