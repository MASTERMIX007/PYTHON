#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 1. Obtener la palabra desde la línea de comandos
# 2. Invertir el orden de las letras de la palabra
# 3. Imprimir la palabra invertida

argumentos = sys.argv[1:]
palabra = argumentos[0]  # ['hola'] -> 'hola'
palabra_lista = list(palabra)  # 'hola' -> ['h', 'o', 'l', 'a']
palabra_lista.reverse()  # ['h', 'o', 'l', 'a'] -> ['a', 'l', 'o', 'h']
palabra_invertida = "".join(palabra_lista)  # ['a', 'l', 'o', 'h'] -> 'aloh'
print(palabra_invertida)


