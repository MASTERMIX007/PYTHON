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
**Ejemplo:** Modifica el script `actores-1.py` para que realice las siguientes operaciones:

1. Imprimea el primer actor de la lista
2. Imprima el último actor de la lista
3. Imprima todos los actores, menos el primero
4. Imprima la lista de actores ordenada alfabéticamente
5. Crea una nueva lista con los actores que inician con `J` e imprimela

---
**Ejercicio:** Modifica el script `actores-2.py` para que realice las siguientes operaciones:

1. Imprimea el 5o actor de la lista
3. Imprima todos los actores, menos el último
4. Imprima la lista de actores ordenada alfabéticamente de la z a la a
5. Crea una nueva lista con los actores que inician con `R` e imprimela

---
**Ejemplo:** Crear el script `lee_inputs.py` que lea e imprima todos los valores proporcionados en la línea de comandos e indique cuántos argumentos o parámetros son en total. Convierte tu escript en ejecutable.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ ./lee_inputs.py Hola
Hola
1 argumentos en total

$ python lee_inputs.py 0.0.0.0
0.0.0.0
1 argumentos en total

$ ./lee_inputs.py 8.8.8.8 8 8.8
8.8.8.8
8
8.8
3 argumentos en total

$ ./lee_inputs.py Hola yo me llamo kiko
Hola
yo
me
llamo
kiko
5 argumentos en total

$ ./lee_inputs.py "Hola yo me llamo kiko"
Hola yo me llamo kiko
1 argumentos en total
```

---
**Ejercicio:** Crear el script `palindromo.py` que lea una palabra desde la línea de comandos e imprima la palabra con la letras en orden inverso, si se obtiene la misma palabra que has escrito, entonces la palabra escrita es un palíndromo. No olvides hacer que tu script sea ejecutable.

A continuación se muestran algunos ejemplos de su ejecución:
  
```sh
$ ./palindromo.py hola
aloh
$ ./palindromo.py osa
aso
$ ./palindromo.py oso
oso
$ ./palindromo.py anilina
anilina
```
¿Podrías encontrar alguna otra palabra que sea un palíndromo? 

---
**Ejercicio:** Crea el script `subred_ipv4.py` que lea desde la línea de comandos una dirección IPV4 y asumiendo que la máscara de red es 255.255.255.0 imprima la dirección IPV4 correspondiente a la subred.

```sh
$ python subred_ip4.py 10.42.0.10
10.42.0.0

$ python subred_ip4.py 192.168.0.1
192.168.0.0

$ python subred_ip4.py 8.8.8.8
8.8.8.0
```
**TIP:** Convierte el texto de la dirección IP a una lista, entonces modifica los elementos de la lista según convenga y luego crea un nuevo texto usando los elementos de la lista.

### Conjuntos (`set()`)

El tipo de dato `set()` se conoce como Conjuntos en Python, es similar al tipo de dato `list()` sólo que no mantiene órden en sus elementos y no puede haber elementos repetidos, es un tipo **Mutable**, ya que se pueden agregar elementos o eliminar elementos. Además los conjuntos permiten realizar las operaciones principales de la teoría de conjuntos como unión, intersección o diferencia.

Una de las aplicaciones más comunes es en el caso de contar con una lista de elementos, donde algunos están repetidos, entonces usando conjuntos es posible eliminar las réplicas, por ejmplo dada la siguiente lista de números:

`[5,7,3,10,13,7,3,8,3,0,5]`

eliminar las réplicas, usar IPython para encontrar el resultado.

### Diccionarios (`dict()`)

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

**Indezación:**

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

---
**Ejemplo:** Modificar el script `superheroes.py` para que imprime la información del super heroe en forma de tabla.

```
python superheroes-1.py 
Name             | Iron Man                                
Realname         | Tony Stark                              
Team             | Avengers                                
Firstappearance  | 1963                                    
Createdby        | Stan Lee                                
Publisher        | Marvel Comics                           
Imageurl         | https://www.simplifiedcoding.net/demos/marvel/ironman.jpg
Bio:
		Anthony Edward Stark, the son of wealthy industrialist and head of Stark Industries, Howard Stark, and Maria Stark. A boy genius, he enters MIT at the age of 15 to study electrical engineering and later receives master's degrees in electrical engineering and physics. After his parents are killed in a car accident, he inherits his father's company.
```

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


