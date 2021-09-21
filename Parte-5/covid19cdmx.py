#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3
import sys

# convierta datos de sqlite3 -> csv

NOMBRE_BD = "datos/covid19-cdmx.sqlite3"

def imprime_csv(lista):
	""" Imprime la lista en la salida estándar en formato CSV """
	writer_csv = csv.writer(sys.stdout)  # para imprimir en pantalla (stdout-> standart output)
	writer_csv.writerows(lista)

with sqlite3.connect(NOMBRE_BD) as con:
	cur = con.cursor()
	# 3. Consulta de datos
	cur.execute("SELECT * FROM Archivo")
	registros = cur.fetchall()
	imprime_csv(registros)



