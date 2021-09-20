#!/usr/bin/env python
# -*- coding: utf-8 -*-


def get_usuarios():
	""" Obtiene la lista de usuarios desde el archivo /etc/passwd """
	NOM_PASSWD = "/etc/passwd"
	arch_usuarios = open(NOM_PASSWD)
	datos = arch_usuarios.read()
	arch_usuarios.close()
	usuarios = datos.splitlines()

	return usuarios

def imprime_tabla(list):
	""" Imprime la lista de usuario en forma de tabla """
	for usr in list:
		alguna_variable = usr.split(":")  # usr -> "halt:x:7:0:halt:/sbin:/sbin/halt"
					# .split(":") -> ["halt","x","7","0","halt","/sbin","/sbin/halt"] -> usr_lst
					# 1o y ultimo: usr_lst[0], usr_lst[-1]
		print(f"{usr[0]:10}{usr[-1]:10}")

def main():
	usuarios_list = get_usuarios()
	imprime_tabla(usuarios_list)

if __name__ == '__main__':
	main()
