#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sqlite3

# convierta datos de sqlite3 -> csv

NOMBRE_BD = "datos/covid19-cdmx.sqlite3"
NOMBRE_CSV = "datos/covid19.csv"

def imprime_csv(lista):
	""" Imprime la lista en la salida estándar en formato CSV """
	with open(NOMBRE_CSV, "w", newline="") as escritor_txt:
		writer_csv = csv.writer(escritor_txt)
		writer_csv.writerows(lista)

with sqlite3.connect(NOMBRE_BD) as con:
	cur = con.cursor()
	# 3. Consulta de datos
	cur.execute("SELECT * FROM Archivo")
	registros = cur.fetchall()
	imprime_csv(registros)
	print("La conversi{on de sqlite3 -> csv a terminado!")



