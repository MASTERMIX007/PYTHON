## Parte-1: Introducción

- ¿Por qué Python?
- Python en el mundo real
- Python 2 vs. Python 3
- Instalar y ejecutar Python

### ¿Por qué Python?

Python se encuentra dentro de los tres primeros lugares en varios raitings de lenguajes de programación, es interpretado, así que apenas se instala se puede comenzar a ejecutar programas y debido a que muchas librerías están creadas en leguaje C tiene un algo grado de eficiencia.

También como parte de su filosofía aporta elementos para simplificar la creación de soluciones con una lógica de lenguaje de muy alto nivel, siendo muy similar a como las personas piensan y no como la máquina piensa, por lo que apoyo muy bien las metodologías ágiles de desarrollo.

Además cuenta con una gran cantidad de librerías como parte de su librería estándar para realizar una gran variedad de tareas en una gran variedad de áreas tan sólo estar instalado, adicionalmente la comunidad de Python agrega unos 300 mil proyectos adicionales que hacen de Python un lenguaje para construir casi lo que se necesite en muy poco tiempo.

La página con proyecto de la comunidad se puede consultar es: https://pypi.org/

### Python en el mundo real

La aplicaciones de Python van desde automatizar tareas a nivel sistema operativo, también a nivel microcontroladores, pasando por redes (Ver casos CISCO designando Python como lenguaje base de desarrollo), entretenimiento, cosmología, ciencias, videjojuegos, aplicacioones de escritorio, aplicaciones web (Instagram o Dropbox), infraescrutura (Ansible), Ciencia de Datos, Machine Learning y mucho más.

Ver el artículo publicado por Netflix acerca de como usa Python, en que áreas y que librerías usa en cada caso: https://www.techrepublic.com/article/how-netflix-uses-python-streaming-giant-reveals-its-programming-language-libraries-and-frameworks/

### Python 2 o Python 3

La versión de Python 2 dejó de tener soporte a partir del 1 de Enero del 2020, así que eso podría poner en riesgo algunas herramientas sobre todo en el área de seguridad, sin embargo esta versión fué ampliamente usada y hoy en día aún existen muchos proyectos que continuan migrando hacia la versión 3 (como es el caso de Ansible).

La versión de Python 3 tiene mejoras que se agradecen como estandarización de las instrucciones del lenguaje a convertirse en funciones u objetos, manejo de Unicode para todo el tratamiento de datos de tipo texto a nivel interno resolviendo así el problema de codificar y decodificar correctamente y contiúa agregando nuevas características como es el uso de f-strins que simplifica el uso de cadenas con formato entre otras cosas más.

Para mayor referencia se puede consultar la página oficial de Python: https://docs.python.org/3/
La página oficial de Python se puede cosnultar en: https://www.python.org

### Instalar y ejecutar Python

**Tipos de instalación**

- Sitio oficial: https://www.python.org
- Usando Miniconda: https://docs.conda.io/en/latest/miniconda.html

Prácticamente todas las distribuciones de Linux hacen uso de una versión de Python para varias tareas administrativas del sistema operativo, así que una manera de no interferir con el Python del sistema es instalar una versión de Python independiente y sin necesidad de contar con permisos de administrador, para ello instalaremos Python con Miniconda.

**Instalando con Miniconda**

Lo primero es entrar a la página y descargar la última versión adecuada para cada sistema operativo, para el caso de Linux y Mac descargar la versión para bash, en el caso de Windows usar el exe correspondiente.

Una vez descargado, en una terminal ejecutar el comando:

```
sh Miniconda3-latest-Linux-x86_64.sh 

Welcome to Miniconda3 py39_4.10.3

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 
```

Aceptar la licencia de uso, seguir las instrucciones y usar las opciones por default si no se está seguro.

Al terminar la instalación, en Linux será necesario salir de la sesión y volver entrar para que los cambios tengan efecto, entonces abrir una termina nuevamente, en el caso de Mac con cerrar todas las ventanas de la terminal abiertas y volviendo a abrir será suficiente, en el caso de Windows, no es necesario, en su lugar hay que iniciar la aplicación llamada **Anaconda Prompt**, entonces lo que se espera es tener un prompt de la siguiente forma:

```
(base)[rctorr][mavi][~/Descargas] $
```

Donde se debe observar el texto `(base)` al inicio del prompt, esto indicará que Python Miniconda se ha instalado de forma correcta.

**Comandos para verificar la instalación de Python**

La versión de Python instalada se puede verificar con:
  
```sh
(base) $ python -V
Python 3.7.4
```

Conociendo la ruta de la instalación:

```sh
$ which python
/home/mi-usuario/miniconda3/bin/python
```

**Iniciando y saliendo del Intérprete de Python**

```sh
$ python
python
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

También se puede salir usando la combinación `Control+D` si tu sistema operativo no lo bloquea.

**Instalando `ipython` que es un intérprete mejorado de Python**

A pesar de que Python busca simplificar y ayudar al usuario en todo lo posible, la comunidad es un gran apoyo y ha creado interpretes de Python mejorados que permiten, siendo uno de ellos `ipython` así que vamos a instalarlo para contar con toda su ayuda, la instalación se realiza con:

```sh
$ pip install ipython
Collecting ipython
Downloading https://files.pythonhosted.org/packages/e7/ba/0ea438e2acd68ce79fde9cf57b4b1f18386969d8a013cd549254b151dde1/ipython-7.17.0-py3-none-any.whl (786kB)
 |████████████████████████████████| 788kB 143kB/s
...
Installing collected packages: ipython
  Found existing installation: ipython 7.13.0
    Uninstalling ipython-7.13.0:
      Successfully uninstalled ipython-7.13.0
Successfully installed ipython-7.17.0
```
    
Verificando la instalación:

```sh
$ ipython
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.17.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: exit()
```

### Hola mundo

Imprimiendo el "Hola mundo!" desde el Intérprete de Python

```sh
$ ipython
Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.17.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: print("Hola mundo de Python!")
Hola mundo de Python!

In [2]:  
```

Imprimiendo el "Hola mundo!" desde un script en Python

Crea el archivo con el nombre `hola-mundo.py` con el siguiente contenido:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

print("Hola mundo de Python en españo!")
```

Y luego ejecuta el archivo o script con:

```sh
$ python hola-mundo.py
Hola mundo de Python en español!
```

Ahora remplaza la siguiente línea:

```python
# -*- coding: utf-8 -*-
```

por:

```python
# -*- coding: latin-1 -*-
```

y ejecuta de nuevo el script ¿observas algún cambio? ¿podrías indicar porque el script imprime el resultado de forma incorrecta?

También podemos hacer que un script en Python sea ejecutable cambiando los permisos de la siguiente forma:

```sh
$ chmod +x hola-mundo.py
```

Entonces ahora podemos ejecutar el script usando la forma:

```sh
$ ./hola-mundo.py
Hola mundo de Python en español!
```

Ahora que sucede si remplazas la línea:

```python
#!/usr/bin/env python
```

por:

```python
#!/usr/bin/env python2.7
```

o por:

```python
#!/usr/bin/env python2.6
```

y ejecutas nuevamente ¿cuál es la diferencia?
