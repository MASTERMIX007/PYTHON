## Parte 4: Estructuras de código

- Comparaciones con if
- Ciclos for y while e Iterar
- Funciones
- Generadores
- Click y los decoradores
- Manejo de errores


### Estructura de control `if-else`

La instrucción `if` nos permite tomar un camino alternativo de ejecución, por ejemplo copia y pega el siguiente código en el sitio [pythontutor](http://www.pythontutor.com/visualize.html#mode=edit).

```python
n = 1
print("Mensaje", n)
n = n + 1
print("Mensaje", n)
n = n + 1
n = n + 1
print("Mensaje", n)
```
    
Examina la ejecución de el código y observa como se ejecuta cada línea y como va cambiando el valor de la variable `n`.

Entonces copia y pega el siguiente código y observa la diferencia:
    
```python
n = 1
print("Mensaje", n)
n = n + 1
print("Mensaje", n)
n = n + 1
if n == 3:
    print("Mensaje", n)
n = n + 1
print("Mensaje", n)
```

Ahora modifica el valor inicial de `n` a `2`, ejecuta de nuevo y observa la diferencia.
    
La instrucción `if-else` nos permite elegir entre dos caminos alternativos.
  
Ahora copia y pega el siguiente código:

```python
n = 1
print("Mensaje", n)
n = n + 1
print("Mensaje", n)
n = n + 1
if n == 3:
    print("Mensaje", n)
else:
    print("Error", n)
n = n + 1
print("Mensaje", n)
```

Modifica el valor inicia de `n` a un valor distinto a 1 y observa como siempre el `if-else` siempre realiza una acción.

---
**Ejemplo:** Ahora vamos a crear el script `lee_entero.py` que lea un número desde la línea de comandos e imprima el valor leído multiplicado por 10 si es un entero, en caso contrario imprima un mensaje de error.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python lee_entero.py 5
50
$ python lee_entero.py 555
5550
$ python lee_entero.py seis
Error e valor de seis no es un entero
$ python lee_entero.py 10.5
Error e valor de 10.5 no es un entero
```

---
**Ejercicio:** Modifica el script `lee_entero.py` para que sólo admita valores hasta 255, en caso contrario que imprima un mensaje de error indicando que el valor es mayor.

```sh
$ python lee_entero.py 256
Error: el valor de 256 es mayor a 255.
```

### Estructura de control `if-elif-else`

La instrucción `if-elif-else` nos permite elegir uno de tres o más caminos en base a las condiciones definidas.
  
Para ver un ejemplo, copia y pega el siguiente código en PythonTutor y modifica el valor inicial de `n` entre los valores de 0, 1, 2, 3 y observa la ejecución.

```python
n = 1
print("Mensaje", n)
n = n + 1
print("Mensaje", n)
n = n + 1
if n == 3:
    print("Mensaje", n)
elif n > 3:
    print("Advertencia: el valor de n es mayor a 3")
else:
    print("Error", n)
n = n + 1
print("Mensaje", n)
```
Comprueba como hay ahora 3 caminos diferentes cuando se ejecuta la instrucción `if-elif-else`.

---
**Ejercicio:** Crea el script `lee_octeto.py` para que sólo admita números enteros en el rango de 0 hasta 255 (un byte), si el número está en el intervalor simplemente lo imprime, en caso contrario que imprima un mensaje de error indicando que el valor no es un octeto.

Ejemplo de ejecución:

```sh
$ python lee_octeto.py 256
Error: el valor de 256 no es un octeto
$ python lee_octeto.py 300
Error: el valor de 300 no es un octeto
$ python lee_octeto.py 128
128
$ python lee_octeto.py 0
0
```

### Estructura de control `for`
La instrucción `for` nos permite repetir un conjunto de instrucciones tantas veces como elementos tenga una lista de elementos.

Copia el siguiente código en PythonTutor y observa el valor de la variable `i`, así como el valor que se va imprimiendo en la salida estándar.

```python
for i in [2, 3, 4.5, "python"]:
    print(i)
```

O también se puede realizar un ciclo para un rango de 10 a 20 por ejemplo:

```python
for i in range(10,21):
    print(i)
```
Nota que se ha colocado 21 y no 20 como límite superior.

---
**Ejemplo:** Crear el script `crash.py` para que realice lo siguiente:

1. Solicitar un número entero al usuario mayor que cero
2. Si el usuario proporciona un valor que no esté en el rango que imprima un mensaje de error
3. Si el usuario proporciona un valor que no sea entero que imprima un mensaje de error
4. Crear una lista con los números enteros desde el 1 hasta el proporcionado por el usuario
5. Imprimir la lista de números en la salida estándar

**ADVERTENCIA:** Este programa no se llama `crash.py` por nada y si tu equipo cuenta con 4 GB o menos es posible que no puedas generar listas de números superiores a 10 millones, con 8GB podrías llegar a 100 o 1 000 millones, la razón es porque la lista de números primero se crea completa, es decir, una lista que incluye los 1000 millones de número por ejemplo y eso se almacena en la memoria RAM, así que podrías monitorear el uso de RAM para evitar que tu sistemae operativo colapse. **FIN DE LA ADVERTENCIA**

A continuación se muestran algunos ejemplos de su ejecución:
```
./crash-rt.py
Dame un número entero mayor que cero [1-...]: 10
Creando lista de números ...
Lista creada!

1
2
3
4
5
6
7
8
9
10
```

---
**Ejemplo:** Modifica el script `crash.py` para que realice lo siguiente:

1. Crea una nueva lista donde cada elemento sea la raíz cuadrada del correspondiente número en la lista original

Ejemplo del resultado:

```
Dame un número entero mayor que cero [1-...]: 10
Creando lista de números ...
Calculando raices ...

1.0
1.4142135623730951
1.7320508075688772
2.0
2.23606797749979
2.449489742783178
2.6457513110645907
2.8284271247461903
3.0
3.1622776601683795
```

---
**Ejemplo:** Crear el script `no-crash.py` para que realice lo siguiente:

1. Solicitar un número entero al usuario mayor que cero
2. Si el usuario proporciona un valor que no esté en el rango que imprima un mensaje de error
3. Si el usuario proporciona un valor que no sea entero que imprima un mensaje de error
4. En lugar de crear una lista con **todos** los números utiliza in *generador* de números como `range()` y crean un rango de número enteros desde el 1 hasta el proporcionado por el usuario.
5. Imprimir la lista de números en la salida estándar

**ADVERTENCIA:** Este programa puede crear adicción ya que puedes crear listas de números tan grande como tu imaginación te lo permita, no importando si tu computadora es del año de Chabelo!

A continuación se muestran algunos ejemplos de su ejecución:
```
./no-crash.py
Dame un número entero mayor que cero [1-...]: 1000000000000

Creando el generador de números ...

1
2
3
4
5
6
7
8
9
10
11
12
13
...
```
Puedes monitorear los recursos ocupados por éste programa y verás que no importa el número que el usuario proporcione, la memoria usada por el programa será la misma.

---
**Ejemplo:** Ahora vamos a crear el script `pyls.py` que haga lo siguiente:

1. Solicite el nombre de una carpeta en la línea de comandos, si el usuario no proporciona una, entonces se usa la carpeta actual (`"."`)
2. Obtener la lista de archivos de la carpeta indicada
3. Imprimir la lista de archivo en la salida estándar
4. Has que tu script sea ejecutable
5. Copia tu script a una carpeta que esté en la variable PATH del sistema
6. Crea una liga simbólica (symbolic link) a tu script con el nombre `pyls`

Ahora ejecuta el script como si fuera un comando más del sistema operativo, por ejemplo:
  
```sh
$ pyls
lee_octeto.py
pyls.py
readme.md

$ pyls /bin
fgconsole
sh.distrib
pidof
kbd_mode
efibootmgr
systemd-tty-ask-password-agent
findmnt
ss
cat
getfacl
readlink
zcmp
lsmod
mt-gnu
dd
...
```

---
**Ejercicio:** Modifica el script `pyls.py` para que también imprima el tamaño de cada archivo en bytes, si es una carpeta imprime el tamaño cero. El tamaño en bytes se puede obtener usando la función `os.path.getsize(nombre)` del mismo módulo `os` ya importado. Para imprimir la lista en forma tabular recuerda hacer uso de las f-strings de Python.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ pyls
   536 lee_octeto.py
  8345 pyls.py
  1255 readme.md
```

### Estructura de control `while`

La instrucción `while` nos permite repetir un conjunto de instrucciones tantas veces como una condición sea verdadera, pudiendo repetir o realizar ciclos que se repiten unas cuantas veces (1, 2, o 3 veces), hasta crear un ciclo infinito.

Copia el siguiente código en PythonTutor y observa como varía el valor de la variable `i` y además observa en que momento es cuando se termina el ciclo `while`

```python
i = 1
while i <= 10:
   print(i)
   i = i + 1
```

---
**Ejemplo:** Ahora vamos a crear el script `el-fin.py` que imprima el mensaje "Desea terminar (S/N)?" y esperará por una respuesta del usuario. Si el usuario responda "S" o "s" o "Si" o "SI" o "sI" el script termina, en caso contrario el script volverá a imprimir el mismo y esperará otra respuesta.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python el-fin.py
Desea terminar (S/N)? n
Desea terminar (S/N)? N
Desea terminar (S/N)? No
Desea terminar (S/N)? y
Desea terminar (S/N)? s
$
```

---
**Ejercicio:** Ahora tienes que crear el script `valida-ip4.py` que realice:

1. Lea una dirección IP4 desde la línea de comandos
2. Realizar las comprobaciones necesarias para determinar si la dirección IP4 es válida o no
3. Imprimir el mensaje "Válidad" si la dirección IP es correcta o el mensaje "Inválidad" en caso contrario.
4. Has tu script ejecutable

**Tip**: Se recomienda hacer uso del método de cadenas `"".split()`, de instrucciones `if` y `for`.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ ./valida-ip4.py 0.0.0.0
Válida
$ ./valida-ip4.py 255.255.0.0
Válida
$ ./valida-ip4.py 127.0.0.1
Válida
$ ./valida-ip4.py 256.255.255.0
Inválida
$ ./valida-ip4.py -8.8.8.8
Inválida
```

### Funciones

En la elaboración de programas a veces existen línea de código que comienzan a repetirse con frecuencia y que tenemos que escribir una y otra vez o si nuestro script comienza a tener muchas líneas, entonces posiblemente nos gustaría poder organizar nuestro script en bloques más pequeños que vayan resolviendo una tarea a la vez, para esto y posiblemente otra razones más es cuando se hace uso de las funciones.

En Python la estructura de una función es la siguiente:

```python
def nombre_funcion(arg1, arg2, ..., argn):
    """ Descripción de la función """
    -bloque de código-
    -de la función-
    
    return -sólo si hay que regresar un valor-
```

Veamos como trabajan las funciones realizando los siguientes ejercicios con IPython:

```python
In [1]: # Creando la función de suma de dos números                             

In [2]: def suma(x, y): 
   ...:     """ Regresa la suma de x más y """ 
   ...:     suma = x + y 
   ...:     return suma 
   ...:                                                                         

In [3]: suma(5, 11)                                                             
Out[3]: 16

In [4]: print(suma(5, 11))                                                      
16

In [4]: total = suma(5, 11)

In [4]: total
16

In [5]: # Creando una función que imprima el total de una operación             

In [6]: def imprime_total(total): 
   ...:     """ Imprime el valor de total con formato """ 
   ...:     print(f"El total de la operación es {total}") 
   ...:                                                                         

In [7]: imprime_total(100)                                                      
El total de la operación es 100

In [8]: imprime_total(1000.50)                                                  
El total de la operación es 1000.5

In [8]: imprime_total(total)                                                  
El total de la operación es 16
```

---
**Ejemplo:** Ahora vamos a modificar el script `pyls.py` para que realice:

1. Con la lista de archivos obtenida, obtenga además la fecha de modificación de cada archivo
2. Teniendo los datos nombre, tamaño y fecha, crea una nueva lista con la siguiente estructura:

```
lista = [
    ["profile", 512, "15-09-2020"],
    ["sistema.sh", 1024, "16-09-2020"],
    ["procedimiento.pdf", 123456, "17-09-2020",
    ["get_pass.pl", 65324, "18-09-2020"
]
```

3. Crea una función llamada `imprime_tabla(lista)` que recibe el parámetro `lista` con los datos de los archivos como se menciona en el punto anterior e imprima la lista de forma tabular con las columnas: **Tamaño**, **Fecha**, **Nombre** y al final imprima el total de bytes usado por todos los archivos.

Ejemplo de ejecución:

```sh
$ ./pyls.py
      1028  17-09-2021  pyls-rt-funciones.py
     17606  17-09-2021  readme.md
       898  16-09-2021  crash-rt.py
       679  17-09-2021  pyls-rt.py
       517  16-09-2021  pyls.py
      4096  15-09-2021  .ipynb_checkpoints
       453  16-09-2021  no-crash-rt.py
       467  16-09-2021  crash.py
      1001  16-09-2021  crash-rt-raiz.py

El total de bytes es de 26745

```

---
**Ejercicio:** Modificar el script `pyls.py` para que la lista de archivos final incluyendo los tres campos sea obtenida por una función llamada `get_archivos(carpeta)`, luego en la zona principal usa la función y asigna el resultado a tu variable `lista`, elimina el código que ya no necesites en la zona principal. 

Ejemplo de ejecución:
```sh
$ ./pyls.py
      1028  17-09-2021  pyls-rt-funciones.py
     17606  17-09-2021  readme.md
       898  16-09-2021  crash-rt.py
       679  17-09-2021  pyls-rt.py
       517  16-09-2021  pyls.py
      4096  15-09-2021  .ipynb_checkpoints
       453  16-09-2021  no-crash-rt.py
       467  16-09-2021  crash.py
      1001  16-09-2021  crash-rt-raiz.py

El total de bytes es de 26745

```

Para más información acerca de la lista de módulos y la lista de funciones de cada módulo se puede consultar la documentación oficial de Python en:
[https://docs.python.org/3/library/index.html](https://docs.python.org/3/library/index.html)


### Generadores

Ya hemos usado generadores, como el caso de `range()`, así que nosotros podemos crear también nuestros generadores para eficientar la ejecución de nuestros programas y primero tenemos que saber que un generador en una función que regresa un valor, generalmente una lista, pero que en lugar de regresa toda la lista de golpe, va regresando elemento a elemento como lo hace `range()`.

En Python la estructura de un generador es el siguiente:

```python
def nombre_generador(arg1, arg2, ..., argn):
    """ Descripción del  generador """
    -bloque de código-
    -de la función-
    -ciclo que genera los valores:-
        -procesamiento de los valores-
        yield -valor a regresar-
```

---
**Ejemplo:** Vamos a crear el script `hola-generadores.py` que construya un generador que realice lo mismo que la función `range(a, b)` que genera los números en el intervalo de `a` hasta `b-1`.

Ejemplo de ejecución para valores de `a=10` y `b=21`:

```sh
$ python hola-generadores.py
10
11
12
13
14
15
16
17
18
19
20

```
Ahora si `a=100000` y b=`2100_000_000`, cuánto tarda en iniciar a imprimir la lista de número?

Veamos como funcionaría un generador tomando como referencia como funcionaría una función primero

---
** Ejemplo:** Crear el script `cuadrados-list.py` que imprima la lista de los cuadrados de los números en el rango de `a` hasta `b-1` creando una función llamada `range_cuadrados(a, b)`.

Ejemplo de resultado para valores de `a=10` y `b=21`:
```sh
$ python cuadrados-list.py 
100
121
144
169
196
225
256
289
324
361
400
```

**Nota:** Si el intervalo de números es muy grande es posible que tu computador colapse cuando la memoria RAM se agote.

Ahora vamos a crear el script `cuadrados-gen.py` como una copia del script `cuadrados-list.py` y luego vamos a modificar la función `range_cuadrados(a, b)` para que se convierta en un generador.

Ejemplo de ejecución con el mismo intervalo:
```sh
$ python cuadrados-gen-rt.py 
100
121
144
169
196
225
256
289
324
361
400
```

Pero ahora podríamos definir el rango que se nos ocurra y el script va a generar la lista sin agostar la memoria RAM, sin embargo considera la desventaja de que si se necesitara ordenar los elementos de la lista sería imposible ya que se genera un elemento, se imprime y se pierde, entonces se pasa al siguiente número, se imprime y se pierde, así que no habría forma de compararlos para ir ordenandolos.

Por ejemplo, si quicieramos aplicar un generador a la función que devuelve la lista de archivos en el script `pyls-2.py`, podría ser útil ya que se podrían procesar listas muy grandes de archivos, pero sólo si no se necesitara ordenar la lista de archivos, algo que seguramente si se va a requerir, así que el uso de generadores no aplicaría para nuestro script o al menos no en este momento.

Así que vamos a aplicarlo creando un script diferente.

---
**Ejemplo:** Crea un script llamado genera-archivos.py que reciba un número entero mayor que cero desde la línea de comando y genere tantos nombres de archivos como el valor de `n` y los nombres tendrán la forma `file-0000001.txt`, `file-0999999.txt` o `file-1000000.txt`

**Nota:** Recuerda hacer uso de funciones y generadores.

Ejemplo de ejecución:

```sh
$ python genera-archivos.py 10
file-0000000001.txt
file-0000000002.txt
file-0000000003.txt
file-0000000004.txt
file-0000000005.txt
file-0000000006.txt
file-0000000007.txt
file-0000000008.txt
file-0000000009.txt
file-0000000010.txt
```

Intenta generar la lista para 1 millón, si has hecho uso correcto de generadores, tu equipo no debería de colapsar, de lo contrario prepárate para un desastre!

Adicionalmente si tuvieras las necesidad de almacenar la lista de archivos generada en un archivo podrías ejecutar el script de la forma:

```
$ ./genera-archivos.py 1000000 > lista_1millon.txt

$ head lista_1millon.txt
file-0000001.txt
file-0000002.txt
file-0000003.txt
file-0000004.txt
file-0000005.txt
file-0000006.txt
file-0000007.txt
file-0000008.txt
file-0000009.txt
file-0000010.txt

$ tail lista_1millon.txt
file-0999991.txt
file-0999992.txt
file-0999993.txt
file-0999994.txt
file-0999995.txt
file-0999996.txt
file-0999997.txt
file-0999998.txt
file-0999999.txt
file-1000000.txt
```

### Creando scripts profesionales usando el módulo `click`

Hasta el momento se han realizado varios script que se pueden ejecutar desde la terminal pero hasta el momento no existe un manual de uso de estos scripts o una opción del tipo `--help`, se pueden agregar y programar, pero ya existen varios módulos que realizan esa tarea y de muy buena forma, para ello se hará uso del módulo `click` que no es parte de la librería estándar, así que su documentación se puede encontrar en la página siguiente:

https://click.palletsprojects.com/en/7.x/

Lo primero es instalar el módulo, para eso realizamos la siguiente instrucción:
```sh
$ pip install click
Collecting click
  Using cached https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl
Installing collected packages: click
Successfully installed click-7.1.2

$
```

---
**Ejemplo:** Vamos a crear el script `hola-click.py` que imprima un saludo al nombre del usuario pasado en la línea de comandos, veamos un ejemplo:

```sh
$ ./hola-click.py Tux
Hola Tux desde Click!

$ ./hola-click.py Octocat
Hola Octocat desde Click!

$ ./hola-click.py
Usage: hola-click.py [OPTIONS] NOMBRE
Try 'hola-click.py --help' for help.

Error: Missing argument 'NOMBRE'.

$
```
Observa como tu script ahora te muestra un mensaje de error indicando la causa, en este caso porque el parámetro `NOMBRE` es obligatorio, pero además nos indica que podemos hacer uso de la opción `--help`, veamos que pasa:

```sh
$ ./hola-click.py --help
Usage: hola-click.py [OPTIONS] NOMBRE

  Imprime un saludo al usuario nombre en la salida estándar

Options:
  --help  Show this message and exit.

$
```
Ahora nuestro escript ya cuenta con toda una funcionalidad como si de un script profesional se tratara, tan sólo con unas cuantas líneas.

---
**Ejemplo:** Ahora copia el script anterior y llámalo `hola-click-n.py` y modifícalo para que cuente con la opción `-n N`, donde N indica la cantidad de veces que será impreso el mensaje en la salida estándar, si la opción no es proporcionada el mensaje de debe imprimir una vez. Veamos un ejemplo:

```sh
$ ./hola-click-n.py Tux
Hola Tux desde Click!

$ ./hola-click-n.py -n 3 Tux
Hola Tux desde Click!
Hola Tux desde Click!
Hola Tux desde Click!

$ ./hola-click-n.py Tux -n 3
Hola Tux desde Click!
Hola Tux desde Click!
Hola Tux desde Click!

$ ./hola-click-n.py --help
Usage: hola-click-n.py [OPTIONS] NOMBRE

  Imprime un saludo al usuario nombre en la salida estándar

Options:
  -n INTEGER  Indica la veces a imprimir el mensaje
  --help      Show this message and exit.

```
observar que ahora en la ayuda ya existe la opción `-n` con el texto descriptivo y todo gracias a `Click`.

---
**Ejemplo:** Vamos a realizar lo siguiente:

1. Copiar el script `pyls-2.py` con el nombre `lss.py`
2. Agregar un función `main()` que ejecute todo el código de la zona principal
3. Converte este script en módulo
4. Incluir el uso del módulo `click`para que realice las mismas tareas.
5. La opción `--help` deberá proporcionar una descripción y ayuda del script.

```sh
$ ./lss.py 
      1038  17-09-2021  pyls-rt-funciones.py
     20768  17-09-2021  readme.md
       898  16-09-2021  crash-rt.py
       679  17-09-2021  pyls-rt.py
       517  16-09-2021  pyls.py
      4096  15-09-2021  .ipynb_checkpoints
       453  16-09-2021  no-crash-rt.py
       467  16-09-2021  crash.py
      1001  16-09-2021  crash-rt-raiz.py
      1027  17-09-2021  pyls-rt-generadores.py

El total de bytes es de 30944

$ ./lss.py --help
Usage: lss.py [OPTIONS] [CARPETA]

  Imprime en la salida estándar la lista de archivo de RUTA, si la ruta no
  se indica se usa la carpeta actual.

Options:
  --help  Show this message and exit.

$
```

---
**Ejemplo:** Modifica el script `lss.py` para agregar la opción `--sort` para que imprima la lista de archivos ordenada alfabéticamente. Algunos ejemplos de ejecución:

```sh
$ ./lss.py --help

$ ./lss-rt.py --sort
      4096  15-09-2021  ./.ipynb_checkpoints/
      1001  16-09-2021  ./crash-rt-raiz.py
       898  16-09-2021  ./crash-rt.py
       467  16-09-2021  ./crash.py
       906  17-09-2021  ./genera-archivos-rt.py
  17000000  17-09-2021  ./lista_1millon.txt
      1500  17-09-2021  ./lss-rt.py
       453  16-09-2021  ./no-crash-rt.py
      1038  17-09-2021  ./pyls-rt-funciones.py
      1027  17-09-2021  ./pyls-rt-generadores.py
       679  17-09-2021  ./pyls-rt.py
       517  16-09-2021  ./pyls.py
     22664  17-09-2021  ./readme.md

El total de bytes es de 17035246
```

---
**Ejercicio:** Modifica el script `lss.py` para agregar la opción `---reverse` para que imprima la lista de archivos ordenada alfabéticamente de forma descendente. Algunos ejemplos de ejecución:

```sh
$ ./lss.py --help
Usage: lss-rt.py [OPTIONS] [CARPETA]

  Imprime la lista de archivoen CARPETA, si CARPETA no se proporciona,
  imprime la lista de archivos de la carpeta actual.

Options:
  --sort     Imprime la lista ordenada alfabéticamente
  --reverse  Imprime la lista ordenada alfabéticamente descendentemente
  --help     Show this message and exit.

./lss-rt.py --sort --reverse
     24059  17-09-2021  ./readme.md
       517  16-09-2021  ./pyls.py
       679  17-09-2021  ./pyls-rt.py
      1027  17-09-2021  ./pyls-rt-generadores.py
      1038  17-09-2021  ./pyls-rt-funciones.py
       453  16-09-2021  ./no-crash-rt.py
      1682  17-09-2021  ./lss-rt.py
  17000000  17-09-2021  ./lista_1millon.txt
       906  17-09-2021  ./genera-archivos-rt.py
       467  16-09-2021  ./crash.py
       898  16-09-2021  ./crash-rt.py
      1001  16-09-2021  ./crash-rt-raiz.py
      4096  15-09-2021  ./.ipynb_checkpoints/

El total de bytes es de 17036823
```

---
**Ejercicio:** Modifica el script `lss.py` para agregar la opción `---sort-size` para que imprima la lista de archivos ordenada en base al tamaño en bytes. Algunos ejemplos de ejecución:

```sh
$ ./lss.py --help
Usage: lss-rt.py [OPTIONS] [CARPETA]

  Imprime la lista de archivoen CARPETA, si CARPETA no se proporciona,
  imprime la lista de archivos de la carpeta actual.

Options:
  --sort       Imprime la lista ordenada alfabéticamente
  --sort-size  Imprime la lista ordenada por tamaño
  --reverse    Imprime la lista ordenada descendentemente
  --help       Show this message and exit.

$ ./lss-rt.py --sort-size --reverse
  17000000  17-09-2021  ./lista_1millon.txt
     25571  17-09-2021  ./readme.md
      4096  15-09-2021  ./.ipynb_checkpoints/
      1906  17-09-2021  ./lss-rt.py
      1038  17-09-2021  ./pyls-rt-funciones.py
      1027  17-09-2021  ./pyls-rt-generadores.py
      1001  16-09-2021  ./crash-rt-raiz.py
       906  17-09-2021  ./genera-archivos-rt.py
       898  16-09-2021  ./crash-rt.py
       679  17-09-2021  ./pyls-rt.py
       517  16-09-2021  ./pyls.py
       467  16-09-2021  ./crash.py
       453  16-09-2021  ./no-crash-rt.py

El total de bytes es de 17038559
```

**Tip:** Para ordenar una lista de listas en base a un campo o elemento de las sublistas como el tamaño que está en la posición `1`, es necesario usar la función `sort()` en la forma:

`lista.sort(key=lambda v: v[N])`

donde `N` es el índice de la posición de la columna o elemento a usar para ordenar, por ejemplo usando un valor de `0` se ordenaría por nombre.

### Manejo de errores

En Python cuando ocurre un error, normalmente el programa se detiene y aparece una lista de mensajes de error devido a que estamos haciendo algo que no está permitido en el lenguaje y en Python estos errores se conocen como **Excepciones**.

Es importante aprender a conocer y manejar las posibles excepciones de nuestros scripts para evitar que se *mueran* en medio de alguna operación y poder tomar una decisión o también para poder enviar un mensaje adecuado al usuario del porque se ha creado cierta excepción.

Para el manejo de excepciones se hace uso de las instrucciones `try-except` de la siguiente manera:
```python
try:
    Bloque de código
    a validar donde podría
    ocurrir una excepción.
except NombreDeLaExcepcion1:
    Bloque de código alternativo a ejecutar
    si la excepción 1 indicada ocurre.
except NombreDeLaExcepcion2:
    Bloque de código alternativo a ejecutar
    si la excepción 2 indicada ocurre.
```

Ahora vamos a ver como funciona con un peque ejemplo usando IPython:
```python
In [1]: a = int("10")                                                           

In [2]: a                                                                       
Out[2]: 10

In [3]: a = int("10.5")                                                         
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-3-6ecad8b0a0fb> in <module>
----> 1 a = int("10.5")

ValueError: invalid literal for int() with base 10: '10.5'

In [7]: try: 
   ...:     a = int("10.5") 
   ...:     print(a) 
   ...: except ValueError: 
   ...:     print("Error: 10.5 no es un entero") 
   ...:                                                                         
Error: 10.5 no es un entero
```

---
**Ejemplo:** Ahora vamos a modificar el script `lee_entero.py` para que realice las mismas funciones, pero el programa no lance excepsiones cuando algún ocurra y en su lugar aparezcan mensaje de error.
  
```sh
$ python lee_entero.py
Error: la forma de usar el script es: lee_entero.py NÚMERO

$ python lee_entero.py uno
Error: el valor proporcionado tiene que ser un número entero

$ python lee_entero.py 10.5
Error: el valor proporcioando tiene que ser un número entero

```

---
**Ejercicio:** Ahora modifica el script `lss.py` para que cuando se indique el nombre de una carpeta que no existe no marque una excepción, si no que se imprima un mensaje de error indicando que la carpeta no existe.

Ejemplo de ejecución:
```sh
$ ./lss.py aaa
Error: la carpeta "aaa" no existe

```

