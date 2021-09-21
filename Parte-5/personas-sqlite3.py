#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect("personas.sqlite3")
cur = con.cursor()

# 1. Creación de tablas
cur.execute("""
	DROP TABLE IF EXISTS Personas
""")

cur.execute("""
	CREATE TABLE Personas (
		id INTERGER PRIMARY KEY,
		nombre VARCHAR(50),
		email VARCHAR(255)
	)
""")
print("Creación de tablas terminado...")

# 2. Agregación de datos
cur.execute("INSERT INTO Personas VALUES (1, 'Tony Stark', 'tony@stark.com')")
cur.execute("INSERT INTO Personas VALUES (2, 'Raul Mixtega', 'mastermix@stark.com')")
cur.execute("INSERT INTO Personas VALUES (3, 'Porqui', 'porqui@stark.com')")
con.commit()
print("Agregación de datos terminado...")

# 3. Consulta de datos
cur.execute("SELECT * FROM Personas")
resp = cur.fetchall()
for linea in resp:
	print(linea)

cur.close()
con.close()



