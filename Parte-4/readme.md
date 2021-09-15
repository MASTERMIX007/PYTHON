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
**Ejemplo:** Ahora vamos a crear el script `pyls.py` que imprima la lista de archivos de una carpeta, si no se proporciona una se imprime la lista de archivos de la carpeta actual. Haz tu script ejecutable y copialo a una carpeta que esté en el PATH.

A continuación se muestran algunos ejemplos de su ejecución:
  
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
**Ejercicio:** Modifica el script `pyls.py` para que también imprima el tamaño de cada archivo en bytes, si es una carpeta imprime el tamaño cero.

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
**Ejercicio:** Ahora tienes que crear el script `lee-ip.py` que lea una dirección IP desde la línea de comandos e imprima el mensaje "Válidad" si la dirección IP es correcta o imprima el mensaje "Inválidad" en caso contrario.

**Nota**: Se recomienda hacer uso del método de cadenas `"".split()` para poder separar cada uno de los octetos.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python lee-ip.py 0.0.0.0
Válida
$ python lee-ip.py 255.255.0.0
Válida
$ python lee-ip.py 127.0.0.1
Válida
$ python lee-ip.py 256.255.255.0
Inválida
$ python lee-ip.py -8.8.8.8
Inválida
```
