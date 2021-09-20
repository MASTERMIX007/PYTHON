#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_range(a, b):
	""" Genera la lista de números enteros en el rango de a a b-1 """
	i = a
	while i < b:
		yield i
		i += 1

for n in mi_range(10, 21):
	print(n)
