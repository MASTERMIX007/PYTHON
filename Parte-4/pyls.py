#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 1. Solicite el nombre de una carpeta en la línea de comandos,
#    si el usuario no proporciona una, entonces se usa la carpeta
#    actual (`"."`)
# 2. Obtener la lista de archivos de la carpeta indicada
# 3. Imprimir la lista de archivo en la salida estándar
# 4. Has que tu script sea ejecutable
# 5. Copia tu script a una carpeta que esté en la variable PATH del sistema
# 6. Crea una liga simbólica (symbolic link) a tu script con el nombre `pyls`

# Tu código aquí!
import os
import sys

# Leer valor de carpeta desde la línea de comandos
if len(sys.argv) == 1:
	carpeta = "."  # carpeta por default
else:
	carpeta = sys.argv[1]

# Obtener lista de archivo de carpeta
archivos = os.listdir(carpeta)

# Imprimir la lista de archivos en la salida estándar
for arch in archivos:
	arch = os.path.join(carpeta, arch)  # /home/kmmx, .mozilla -> /home/kmmx/.mozilla
	tam = os.path.getsize(arch)
	print( f"{tam:10}  {arch}" )








