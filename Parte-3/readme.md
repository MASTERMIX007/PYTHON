## Parte 3: Listas, Tuplas, Diccionarios y Conjuntos

- Listas y Tuplas
- Conjuntos
- Diccionarios
- Crear estructuras grandes de Datos

### Listas y tuplas (`list() y tuple()`)

El tipo de datos `list()` se conoce como Listas en Python, es similar al tipo de datos `array` de otros lenguajes de programación, así que una lista es una colección de datos no necesariamente del mismo tipo (como en el caso de los arreglos) con un órden determinado, además cada elemento de la lista puede ser modificado, por esta razón en Python se dice que las listas son un tipo **Mutable**.

Las tuplas `tuple()` son similares a las listas, sólo que son **Inmutables**, o sea que una vez creadas no se pueden modificar, así que no es posible alterar el orden de los elementos, agregar nuevos, eliminar o modificar.

A continuación se muestras varias maneras de inicializar o crear una lista y una tupla haciendo uso de IPython para obtener un resultado de forma inmediata:

```python
In [1]: # Creando una lista de 5 enteros
In [2]: [3,7,2,6,7]
Out[2]: [3, 7, 2, 6, 7]

In [3]: # Creando una lista de 5 números decimales
In [4]: [1.2, 2.3, 4.5, 5.1, 6.2]
Out[4]: [1.2, 2.3, 4.5, 5.1, 6.2]

In [5]: # Creando una lista de 5 palabras
In [6]: ["Hola", "listas", "en", "Python", "!"]
Out[6]: ['Hola', 'listas', 'en', 'Python', '!']

In [7]: # Creando una lista campechana de 5 elementos 
In [9]: ["a", 3, 2.5, 10/3, "-Fin-"*5]
Out[9]: ['a', 3, 2.5, 3.3333333333333335, '-Fin--Fin--Fin--Fin--Fin-']
```

También se puede crear una lista vacía:
```python
In [10]: []
Out[10]: []

In [11]: list()
Out[11]: []
```

Para el caso de las tuplas es similar:
```python
In [1]: # Creando una tupla de 5 enteros
In [2]: (3,7,2,6,7)
Out[2]: (3, 7, 2, 6, 7)

In [3]: # Creando una tupla de 5 números decimales
In [4]: (1.2, 2.3, 4.5, 5.1, 6.2)
Out[4]: (1.2, 2.3, 4.5, 5.1, 6.2)

In [5]: # Creando una tupla de 5 palabras
In [6]: ("Hola", "listas", "en", "Python", "!")
Out[6]: ('Hola', 'listas', 'en', 'Python', '!')

In [7]: # Creando una tupla campechana de 5 elementos 
In [9]: ("a", 3, 2.5, 10/3, "-Fin-"*5)
Out[9]: ('a', 3, 2.5, 3.3333333333333335, '-Fin--Fin--Fin--Fin--Fin-')
```

También se puede crear una tupla vacía:

```python
In [10]: ()
Out[10]: ()

In [11]: tuple()
Out[11]: ()
```

### Operaciones con listas y tuplas

Las operaciones que se pueden realizar con listas y tuplas son las siguientes:

- Suma o concatenación: `+`
- Multiplicación o replicación: `*`
- Indezación: `[]`
- Rebanadas o slices: `[a:b]`
- Obtener longitud: `len(lista o tupla)`
- Adición: `+=`
- Métodos tuplas:
  - `.count()`
  - `.index()`
- Métodos listas:
  - `.append()`
  - `.copy()`
  - `.count()`
  - `.index()`
  - `.reverse()`
  - `.sort()`
- Modificanción listas: `lista[indice]=nuevo_valor`

Realizar algunos ejemplos con IPython para observar el comportamiento.

**Nota:** Observar como todas las operaciones donde se modifica el contenido de una lista como ordenar o modificar una lista no es posible realizarlas con una tupla.

---
**Ejemplo:** Crear el script `lee_inputs.py` que lea e imprima todos los valores proporcionados en la línea de comandos e indique cuántos argumentos o parámetros son en total.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python lee_inputs.py Hola
Hola
1 argumentos en total

$ python lee_inputs.py 0.0.0.0
0.0.0.0
1 argumentos en total

$ python lee_inputs.py 8.8.8.8 8 8.8
8.8.8.8
8
8.8
3 argumentos en total

$ python lee_inputs.py Hola yo me llamo kiko
Hola
yo
me
llamo
kiko
5 argumentos en total

$ python lee_inputs.py Hola yo me llamo kiko
Hola <- str
yo <- str
me <- str
llamo <- str
kiko <- str
5 argumentos en total

$ python lee_inputs.py "Hola yo me llamo kiko"
Hola yo me llamo kiko
1 argumentos en total
```

---
**Ejemplo:** Ahora vamos a crear el script `valida_palindromo.py` que lea una valor desde la línea de comandos e imprima True (Verdadero) si el valor corresponde a una palabra palíndromo, que son aquellas palabras que se leen igual de derecha a izquierda y de izquierda a derecha, de lo contrario deberá imprimir False (Falso).

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python valida_palindromo.py Hola
False
$ python valida_palindromo.py Osa
False
$ python valida_palindromo.py Oso
True
$ python valida_palindromo.py Anilina
True
```

---
**Ejercicio:** Crea el script `valida_ip4_192.168.1.py` que lea desde la línea de comandos un argumento e imprima `True` si la IP4 pertenezcan a la subred `192.168.1.0`, de lo contrario imprime `False`.

```sh
$ python valida_ip4_192.168.1.py 256.255.255.0
False

$ python valida_ip4_192.168.1.py 192.168.0.1
False

$ python lee_ip4_192.168.1.py 192.168.1.83
True
```

---
**Ejemplo:** Dada una lista de 5 nombres de archivos, crea el script `logitud_nombres.py` que imprima el nombre de cada uno y enseguida su longitud.

```
archivos = (
    "sublime_text_build_4113_mac.zip",
    "Tabulado.csv",
    "Telegram Desktop",
    "terminal-cheatsheet.zip",
    "Typora-linux-x64.tar.gz"
)
```

```sh
$ python longitud_nombres.py
sublime_text_build_4113_mac.zip 31
Tabulado.csv 12
Telegram Desktop 16
terminal-cheatsheet.zip 23
Typora-linux-x64.tar.gz 23
```

### Conjuntos (`set()`)

El tipo de dato `set()` se conoce como Conjuntos en Python, es similar al tipo de dato `list()` sólo que no mantiene órden en sus elementos y no puede haber elementos repetidos, es un tipo **Mutable**, ya que se pueden agregar elementos o eliminar elementos. Además los conjuntos permiten realizar las operaciones principales de la teoría de conjuntos como unión, intersección o diferencia.

Una de las aplicaciones más comunes es en el caso de contar con una lista de elementos, donde algunos están repetidos, entonces usando conjuntos es posible eliminar las réplicas, por ejmplo dada la siguiente lista de números:

`[5,7,3,10,13,7,3,8,3,0,5]`

eliminar las réplicas, usar IPython para encontrar el resultado.

### Tipo de dato `dict()`

El tipo de dato `dict()` se conoce como Diccionarios (o dict) en Python, es similar al tipo de datos `struct` u `object` de otros lenguajes de programación, así que un Diccionario es una colección de parejas de datos (llave:valor) no necesariamente del mismo tipo sin un órden determinado, cada elemento puede ser modificado por lo que es un tipo de dato **Mutable**. Los diccionarios se usan cuando se requiere de asignar nombre a cada elemento de la colección en lugar de usar índices núméricos como el caso de las listas.

La forma general de construir un Diccionario es la siguiente:
```python
{
    llave_1:valor_1,
    llave_2:valor_2,
    llave_3:valor_3,
    ...
    llave_n:valor_n,
}
```
Las llaves pueden ser cualquier tipo de datos básico (`int`, `float` o `str`), el valor puede ser de cualquier tipo de dato, ya sea básico o de tipo collección.

A continuación se muestras varias maneras de inicializar o crear un Diccionario haciendo uso de IPython para obtener un resultado de forma inmediata:

```python
In [1]: # Creando un diccionario de 3 elementos
In [2]: {"campo_1":"valor 1", "campo_2": 2, "campo_3": 3.0}
Out[2]: {'campo_1': 'valor 1', 'campo_2': 2, 'campo_3': 3.0}
    
In [3]: # Creando un diccionario con valores tipo lista y diccionario
In [4]: {"lista":[1,2,3,4,5], "dicc":{"uno":1, 2:2, 3.0:"tres"}}
Out[4]: {'lista': [1, 2, 3, 4, 5], 'dicc': {'uno': 1, 2: 2, 3.0: 'tres'}}

In [5]: # Creando un diccionario para representar a un archivo
In [6]: {"nombre":"archivo_1.ext", "ext":".ext", "tamanio":12345, "fecha_de_creacion":"15-09-2020"}
Out[6]: 
{'nombre': 'archivo_1.ext',
 'ext': '.ext',
 'tamanio': 12345,
 'fecha_de_creacion': '15-09-2020'}
```
También se puede crear un Diccionario vacío:
```python
In [10]: {}
Out[10]: {}

In [11]: dict()
Out[11]: {}
```
Para acceder a los elementos de un Diccionario hacemos uso de la llave que es el índice con el que podemos acceder a algún valor, veamos algunos ejemplos:
```python
In [12]: dict_1 = {"campo_1":"valor 1", "campo_2": 2, "campo_3": 3.0}

In [13]: dict_1["campo_1"]
Out[13]: 'valor 1'

In [14]: dict_1["campo_2"]
Out[14]: 2

In [15]: dict_1["campo_3"]
Out[15]: 3.0

In [16]: dict_2 = {"lista":[1,2,3,4,5], "dicc":{"uno":1, 2:2, 3.5:"tres"}}
Out[16]: 7

In [17]: dicto_2["lista"]
Out[17]: [1, 2, 3, 4, 5]

In [18]: dict_2["dicc"]                                                          
Out[18]: {'uno': 1, 2: 2, 3.0: 'tres'}

In [8]: dict_2["dicc"]["uno"]                                                   
Out[8]: 1

In [14]: dict_2["dicc"][3.5]                                                    
Out[14]: 'tres'

In [15]: dict_2["dicc"][3]                                                      
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-15-18f83cf4d0be> in <module>
----> 1 dict_2["dicc"][3]

KeyError: 3
```
Se observa como al final al intentar acceder al elemento la llave 3, Python muestra un error porque la llave 3 no existe.

### Diccionarios

Los diccionarios en Python, son un tipo de dato muy flexible que permite almacenar valores usando una llave como referencia, así que por cada valor se necesita de una llave, no mantienen un orden de los elementos, pero si son mutables.

A continuación se muestras varias maneras de inicializar o crear un diccionario haciendo uso de IPython para obtener un resultado de forma inmediata:

```python
In [1]: # Creando un diccionario de 5 elementos
In [2]: {0:"cero", 1:"uno", 2:"dos", 3:"tres", 4:"cuatro"}
Out[2]: {0: 'cero', 1: 'uno', 2: 'dos', 3: 'tres', 4: 'cuatro'}

In [3]: # Creando un diccionaro con llaves de tipo cadena
In [4]: {"cero": 0, "uno":1, "dos":2, "tres":3, "cuatro": 4}
Out[4]: {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}

In [5]: # Creando un diccionario mixto
In [6]: {'cero': 0, 1: "uno", 2.5: "decimal", 'lista': [1,2,3]}
Out[6]: {'cero': 0, 1: 'uno', 2.5: 'decimal', 'lista': [1, 2, 3]}
```

También se puede crear un diccionario vacío con:
```python
In [10]: {}
Out[10]: {}

In [11]: dict()
Out[11]: {}
```

### Operaciones con diccionarios

Las operaciones que se pueden realizar con diccionarios son las siguientes:

- Indezación: `[]`
- Obtener longitud: `len(diccionario)`
- Métodos diccionarios:
  - `.copy()`
  - `.get()`
  - `.items()`
  - `.keys()`
  - `.update()`
  - `.values()`
- Agregar nuevos elementos: `dict[llave]=valor`
- Modificanción diccionarios: `dict[llave]=nuevo_valor`

Realizar algunos ejemplos con IPython para observar el comportamiento.

---
**Ejemplo:** Ahora vamos a crear el script `lee_archivo.py` que lea e imprima los datos de un archivo pasados desde la línea de comandos como se indica a continuación:
```
Sintaxis:

lee_archivo.py NOMBRE TAMAÑO
```
Luego el script deberá imprimir como resultado un diccionario incluyendo el nombre, extensión y tamaño.
```
{
    "nombre": "nombre_archivo.ext",
    "ext": "ext",
    "tamanio": 12345
}
```

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ python lee_archivo.py passwd 512
{
    "nombre":"passwd",
    "ext":"",
    "tamanio":512
}

$ python lee_archivo.py proceso.sh 1024
{
    "nombre":"proceso.sh",
    "ext":"sh",
    "tamanio":1024
}
```
Recuerda hacer uso de las funciones `int()` o `split()` para obtener la extensión y convertir el tamaño en entero.

---
**Ejercicio:** Modifica el script `imprime_archivos.py` para que imprima la lista de archivo ya contenida en el script en forma tabular.

Ejemplo de ejecución:
```sh
$ python imprime_archivos.py
profile                     512 15-09-2020     
sistema.sh                 1024 16-09-2020     
procedimiento.pdf        123456 17-09-2020     
get_pass.pl               65324 18-09-2020     
```


