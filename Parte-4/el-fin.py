#!/usr/bin/env python
# -*- coding: utf-8 -*-

no_terminar = True
while no_terminar == True:
	respuesta = input("Desea terminar (S/N)? ")
	if respuesta.lower() == "s":  # s->s, S->s
		no_terminar = False
	elif respuesta.lower() == "si":  # si->si, SI->si, Si->si, sI->si
		no_terminar = False
print("Respuesta correcta de salida!")