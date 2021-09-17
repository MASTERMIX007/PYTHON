#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# 1. Leer la dirección IP4 desde la línea de comandos "8.8.8.8", "10.42.0.10"
# 2. Obtener los primeros 3 octetos 
# 3. Agregar el cuarto octeto con valor de cero (ip de subred)
# 4. Imprimir la dirección de la subred

# (a)
# argumentos = sys.argv[1:]  # ["8.8.8.8"] | ["10.42.0.10"]
# ip4 = argumentos[0]  # "8.8.8.8" | "10.42.0.10"

# (b)
# ip4_list = ip4.split(".")  # ["8", "8", "8", "8"]
# del(ip4_list[-1])  #  ["8", "8", "8"] | ip4_list[:3]
# # ip4_list = ["8", "8", "8"]
# ip4_list.append("0")  # ["8", "8", "8", "0"]

# (c)
# ip4_4 = ".".join(ip4_list)  # "8.8.8.0"
# print(ip4_list)

ip4 = (sys.argv[1:])[0]  # (a)
#     ^^^^^^^^^^^^|||
ip4_list = ip4.split(".")[:3] + ["0"]  # (b)
#          ^^^^^^^^^^^^^^|||| !!!!!!!
print(".".join(ip4_list))  # (c)


