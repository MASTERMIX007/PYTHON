#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import openpyxl

# zona de funciones
def max_ancho(filas, i):
    """ Calcula el ancho máximo de filas en la columna i """
    columna_i = [f[i] for f in filas]
    ancho_i = [0 if f == None else len(f) for f in columna_i]
    
    return max(ancho_i)


def imprime_txt(filas):
    """
    Imprime las filas en la salida estándar en formato texto
    """
    anchos = []
    for i, col in enumerate(filas[0]):
        anchos.append( max_ancho(filas, i) )
    
    for fila in filas:
        linea = []
        for i, val in enumerate(fila):
            if val == None:
                linea.append(f"{'':{anchos[i]}}")
            else:
                linea.append(f"{val:{anchos[i]}}")
        linea_str = "  ".join(linea)
        print(linea_str)

def get_datos_xlsx(archivo):
    """ Obtiene la de filas de archivo en formato xlsx """
    wb_obj = openpyxl.load_workbook(archivo)  # abrir el libro de trabajo
    # wb_obj <- representa el archivo en xlsx
    sheet = wb_obj.active  # regresa la hoja de trabajo activa del documento
    # sheet <- representa una hoja
    filas = []  # <- guarda todas las filas de la hoja
    for row in sheet.iter_rows():
        fila = []  # <- guarda todas las celdas de la fila
        for cell in row:
            fila.append(cell.value)
        filas.append(fila)

    return filas
    

# type=click.Path(exists=True) <- sirve para validar si el archivo a usar existe o no

@click.command()
@click.argument("archivo", type=click.Path(exists=True))
def main(archivo):
    """
    Imprime el contenido de ARCHIVO que está en formato binario XLSX
    """
    filas_xlsx = get_datos_xlsx(archivo)
    imprime_txt(filas_xlsx)

# Condición para que el main() sólo se ejecute como script
if __name__ == '__main__':
    main()


