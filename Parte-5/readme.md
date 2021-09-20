## Parte 5 – Manejo de Datos

- Archivos de texto
- Archivos de texto estructurados (CSV)
- Archivos binarios estructurados
- Bases de datos relacionales (SQL)
- Introducción a almacenamiento de datos NoSQL (JSON)


### Archivos

El poder leer información desde un archivo o escribir información en un archivo es algo escencial en cualquier lenguaje de programación ya que nos permite que los datos se vuelvan persistentes.

En Python para poder abrir un archivos para lectura o escritura de hacer uso de la instrucción `open(nombre_archivo, modo)`, donde `nombre_archivo` es el nombre y ruta donde está ubicado el archivo, si el archivo no existe o la ruta es erronea aparecerá una excepción, `modo` puede ser `r` (read) lectura y es el modo por omisión, también puede ser `w` (write) o `wb` (write binary) o `a` (append), estás últimas permiten escribir o agregar datos a un archivo.

Realiza los siguientes ejemplo haciendo uso de IPython:
```python
In [1]: archivo_1 = open("readme.md")                                 

In [2]: for linea in archivo_1: 
   ...:     print(linea) 
   ...:                                                                         
## Parte 4: Estructuras de código

- Comparaciones con if
- Ciclos for y while e Iterar
- Funciones
...

In [3]: archivo_1.close()                                                       

In [4]:  

```

Ahora un ejemplo con la forma recomendada para leer archivo con Python:
```python
In [4]: with open("/etc/passwd", "r") as arch: 
   ...:     texto = arch.read() 
   ...:                                                                         

In [5]: texto                                                                   
Out[5]: 'root:x:0:0:root:/root:/bin/bash\ndaemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\nbin:x:2:2:bin:/bin:/usr/sbin/nologin\nsys:x
...   user,,,:/var/run/hplip:/bin/false\ngeoclue:x:121:127::/var/lib/geoclue:/usr/sbin/nologin\nrctorr:x:1000:1000:rctorr,,,:/home/rctorr:/bin/bash\nsshd:x:122:65534::/run/sshd:/usr/sbin/nologin\nmysql:x:123:129:MySQL Server,,,:/nonexistent:/bin/false\n'

In [6]: print(texto)                                                            
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
...
rctorr:x:1000:1000:rctorr,,,:/home/rctorr:/bin/bash
sshd:x:122:65534::/run/sshd:/usr/sbin/nologin
mysql:x:123:129:MySQL Server,,,:/nonexistent:/bin/false


In [7]: texto.splitlines()                                                      
Out[7]: 
['root:x:0:0:root:/root:/bin/bash',
 'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin',
 'bin:x:2:2:bin:/bin:/usr/sbin/nologin',
...
 'rctorr:x:1000:1000:rctorr,,,:/home/rctorr:/bin/bash',
 'sshd:x:122:65534::/run/sshd:/usr/sbin/nologin',
 'mysql:x:123:129:MySQL Server,,,:/nonexistent:/bin/false']

In [10]: for u in texto.splitlines(): 
    ...:     print(u) 
    ...:                                                                        
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
...
rctorr:x:1000:1000:rctorr,,,:/home/rctorr:/bin/bash
sshd:x:122:65534::/run/sshd:/usr/sbin/nologin
mysql:x:123:129:MySQL Server,,,:/nonexistent:/bin/false
```

---
**Ejercicio:** Crear el script `imprime_passwd.py` para que imprima el user y el shell asignado de la lista de usuarios contenida en el archivo `/etc/passwd`. Para ello se deberán crear dos funciones, `get_usuarios()` que deberá regresar una lista de usuarios, donde cada elemento de la lista será un usuario con los campo solicitados e `imprime_usuarios()`, que recibe una lista de usuarios los imprime en forma de tabla incluyendo sólo los campos user y shell.

Ejemplo de ejecución:
```sh
$ python imprime_usuarios.py
root     /bin/bash
daemon   /usr/sbin/nologin
bin      /usr/sbin/nologin
...
rctorr   /bin/bash
sshd     /usr/sbin/nologin
mysql    /bin/false
```

### Archivos de texto estructurados (CSV)

Nuestros módulos no necesariamente son estáticos ya que podemos continuar agregando funciones, en este caso vamos a hacer que el script imprima los resultados en la salida estándar, pero en un forma diferente, por ejemplo CSV.

---
**ACTIVIDAD:** Vamos a modificar el script `archivos.py` para agregar la función `imprime_csv()` que imprima la lista de archivos en la salida estándar en formato CSV haciendo uso de la opción `--csv`

Ejemplo de ejecución:
```sh
$ python archivos.py --csv
profile,512
sistema.sh,1024
procedimiento.pdf,123456
get_pass.pl,65324

$ 
```

### Archivos en formato JSON

Hasta el momento hemos estado manejando archivos de tipo texto plano o archivos en formato CSV que también son archivos de texto, pero que siguen siertas reglas, ahora vamos a revisar otro tipo de formato de archivos de texto conocido como JSON y que también es muy usado para el intercambio de información.

Para simplificar la manipulación de archivos en formato JSON en Python existe el módulo `json` y su documentación puede ser consultada en:

https://docs.python.org/3/library/json.html

Primero vamos a conocer como funciona el módulo y como podemos importar datos desde y hacia el formato JSON.

A continuación tenemos un ejemplo de tipos de datos en formato JSON, observa que es texto, si lo comparamos con el formato CSV, los datos son acomodados en forma de tabla, mientras que en JSON son acomodados en forma **jerárquica**.

Hay que tomar en cuenta que el forma JSON tiene sus orígenes en el lenguaje Javascript, así que la intención de ese formato es poder representar los valores de los tipos de datos que existen en ese lenguaje como son:

- null
- true y false
- number (int y real)
- string
- array
- object

Veamos el siguiente ejemplo:
```json
[
    {
        "id":1,
        "tarea": "Comprar pan de muerto",
        "terminada": false,
        "fecha_creada": "2020-10-20",
        "fecha_terminada": ""
    },
    {
        "id":2,
        "tarea": "Llevar un pan de muerto a tú",
        "terminada": false,
        "fecha_creada": "2020-10-20",
        "fecha_terminada": ""
    },
    {
        "id":3,
        "tarea": "Preparar código para clase",
        "terminada": true,
        "fecha_creada": "2020-10-20",
        "fecha_terminada": "2020-10-20"
    }
]
```
Los corchetes `[...]` son un array y su equivalente en Python será una lista.

Las llaves `{...}` son un object y su equivalente en Python será un diccionario y los datos se organizan mediante el esquema de llave:valor.

El formato `-llave-:-valor-` es la forma más común en que los datos son representado en un documento JSON donde `-llave-` es una etiqueta que permite localizar el `-valor` relacionado y generalmente es de tipo string, mientras que el `-valor-` puede ser de cualquiera de los tipos de datos mencionados anteriormente.

El módulo `json` al importar datos desde JSON a Python realiza las siguientes conversiones:

- null -> None
- true y false -> True, False
- number (int y real) -> int, float
- string -> str
- array -> list
- object -> dict

Ahora veamos como se realiza la importación usando IPython e inicamos copiando los datos en una variable de tipo texto o `str`:
```python
In [2]: datos_json = """ 
   ...: [ 
   ...:     { 
   ...:         "id":1, 
   ...:         "tarea": "Comprar pan de muerto", 
   ...:         "terminada": false, 
   ...:         "fecha_creada": "2020-10-20", 
   ...:         "fecha_terminada": "" 
   ...:     }, 
   ...:     { 
   ...:         "id":2, 
   ...:         "tarea": "Llevar un pan de muerto a tú", 
   ...:         "terminada": false, 
   ...:         "fecha_creada": "2020-10-20", 
   ...:         "fecha_terminada": "" 
   ...:     }, 
   ...:     { 
   ...:         "id":3, 
   ...:         "tarea": "Preparar código para clase", 
   ...:         "terminada": true, 
   ...:         "fecha_creada": "2020-10-20", 
   ...:         "fecha_terminada": "2020-10-20" 
   ...:     } 
   ...: ] 
   ...: """                                                                     
In [3]: type(datos_json)                                                        
Out[3]: str

In [4]: import json                                                             

In [5]: datos = json.loads(datos_json)                                          

In [6]: datos                                                                   
Out[6]: 
[{'id': 1,
  'tarea': 'Comprar pan de muerto',
  'terminada': False,
  'fecha_creada': '2020-10-20',
  'fecha_terminada': ''},
 {'id': 2,
  'tarea': 'Llevar un pan de muerto a tú',
  'terminada': False,
  'fecha_creada': '2020-10-20',
  'fecha_terminada': ''},
 {'id': 3,
  'tarea': 'Preparar código para clase',
  'terminada': True,
  'fecha_creada': '2020-10-20',
  'fecha_terminada': '2020-10-20'}]

In [7]:  
```
Se ha hecho uso de la función `json.loads(-variabel de texto-)` del módulo `json` y lo que hace es cargar o importar una cadena con datos en formato JSON y transformarlo en tipos de datos Python, el resultado puede ser guardado en una variable, en este caso la variable `datos`

Ahora vamos a indagar que tipos de datos tenemos y como podermos acceder a ellos.
```python
In [7]: type(datos)                                                             
Out[7]: list

In [8]: 
```
Como la variable `datos` es una lista, entonces podemos acceder a sus elementos mediante un índice o mediante un ciclo `for`:
```python
In [8]: datos[0]                                                                
Out[8]: 
{'id': 1,
 'tarea': 'Comprar pan de muerto',
 'terminada': False,
 'fecha_creada': '2020-10-20',
 'fecha_terminada': ''}

In [9]: datos[1]                                                                
Out[9]: 
{'id': 2,
 'tarea': 'Llevar un pan de muerto a tú',
 'terminada': False,
 'fecha_creada': '2020-10-20',
 'fecha_terminada': ''}

In [10]: for elemento in datos: 
    ...:     print(elemento) 
    ...:                                                                        
{'id': 1, 'tarea': 'Comprar pan de muerto', 'terminada': False, 'fecha_creada': '2020-10-20', 'fecha_terminada': ''}
{'id': 2, 'tarea': 'Llevar un pan de muerto a tú', 'terminada': False, 'fecha_creada': '2020-10-20', 'fecha_terminada': ''}
{'id': 3, 'tarea': 'Preparar código para clase', 'terminada': True, 'fecha_creada': '2020-10-20', 'fecha_terminada': '2020-10-20'}

In [11]:  
```
Se puede observar que cada elemento de datos corresponde a los datos del registro de una tarea, así que ahora vamos a analizar el primer elemento de la lista:
```python
In [11]: tarea = datos[0]                                                       

In [12]: type(tarea)                                                            
Out[12]: dict

In [13]: tarea                                                                  
Out[13]: 
{'id': 1,
 'tarea': 'Comprar pan de muerto',
 'terminada': False,
 'fecha_creada': '2020-10-20',
 'fecha_terminada': ''}

In [14]:  
```
Entonces nuestra variable `tarea` es de tipo `dict` y al imprimir su contenido vemos que tiene las llaves:
- `id` que es el identificador de cada tarea
- `tarea` que es la descripción de la tarea
- `fecha_creada` que es la fecha en que fué agregada
- `fecha_terminada` que es cuando la tarea fué finalizada

Así que ahora podríamos obtener cada valor de cada una de las llaves o incluso modificar alguno de los valores si fuera necesario:
```python
In [20]: tarea["id"]                                                            
Out[20]: 1

In [21]: tarea["tarea"]                                                         
Out[21]: 'Comprar pan de muerto'

In [22]: tarea["terminada"]                                                     
Out[22]: False

In [23]: print("{id:02} | {terminada:5} | {tarea}".format(**tarea))             
01 |     0 | Comprar pan de muerto

In [24]: tarea["terminada"] = True                                              

In [25]: print("{id:02} | {terminada:5} | {tarea}".format(**tarea))             
01 |     1 | Comprar pan de muerto

In [24]: tarea["terminada"] = True                                              

In [29]: print("{id:02} | {terminada!s:5} | {tarea}".format(**tarea))           
01 | True  | Comprar pan de muerto

```

---
**ACTIVIDAD** Crea el script `lee-json.py NOMBRE` para que lea el contenido del archivo NOMBRE en formato JSON y lo imprima en la salida estándar.

```sh
$ python lee-json.py anime.json
Usage: lee-json.py [OPTIONS] NOMBRE

  Lee el contenido de NOMBRE en formato JSON y lo imprime en la salida
  estándar

Options:
  --help  Show this message and exit.

$ python lee-json.py anime.json 
{
    "data": [
        {
            "id": "1",
            "type": "anime",
            "links": {
                "self": "https://kitsu.io/api/edge/anime/1"
            },
...
    "links": {
        "first": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=0",
        "prev": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=0",
        "next": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=10",
        "last": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=13787"
    }
}

$
```
También se podría haber usando el módulo `json` de forma directa:
```sh
$ python -m json.tool anime.json 
{
    "data": [
        {
            "id": "1",
            "type": "anime",
            "links": {
                "self": "https://kitsu.io/api/edge/anime/1"
            },
...
    "links": {
        "first": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=0",
        "prev": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=0",
        "next": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=10",
        "last": "https://kitsu.io/api/edge/anime?page%5Blimit%5D=10&page%5Boffset%5D=13787"
    }
}

$
```
O sea que con sólo tener Python instalado se puede imprimir de forma indentada un archivos en formato JSON, pero si se dea realizar alguna tarea a nivel datos de esta forma no es posible, pero Python siempre al servicio de la comunidad!.

---
**ACTIVIDAD** Crea el script `anime-json.py` para que lea el contenido del archivo `anime.json` e imprima en la salida estándar el `id`, `título` y `link poster original`

```sh
$ python anime-json.py
id: 1
titulo: Cowboy Bebop
Poster original: https://media.kitsu.io/anime/poster_images/1/original.jpg?1431697256
```
Y como actividad adicional, podrías abrir el link a la imagen para ver el poster!

---
**RETO** Modifica el script `anime-json.py` para que incluya el link de la portada original.

```sh
$ python anime-json.py
id: 1
titulo: Cowboy Bebop
Poster original: https://media.kitsu.io/anime/poster_images/1/original.jpg?1431697256
Portada original: https://media.kitsu.io/anime/cover_images/1/original.jpg?1416336000
```
Y como actividad adicional, podrías abrir el link a la imagen para ver la portada!

---
---
### Convirtiendo archivos de formato CSV a JSON

Una de las tareas para las que Python es muy muy bueno es la de procesar datos de tipo texto y en particular en dos formatos ampliamente conocidos CSV y JSON.

Por lo que haciendo uso de los módulos `csv` y `json` vamos a crear un script que transforme cada registro del archivo CSV a uno o varios objetos en JSON, así que primero tenemos que **definir** como se realizará esta transformación.

En un archivo CSV por lo general existe una primer fila que contiene el nombre de cada columna, así que eso puede servir de base para obtener el nombre de cada campo, además cada fila representa un registro entonces la propuesta es dado un archivo CSV (`datos/covid19-cdmx.csv`):

```csv
"FECHA_ACTUALIZACION","ID_REGISTRO","ORIGEN","SECTOR","ENTIDAD_UM","SEXO","ENTIDAD_NAC","ENTIDAD_RES","MUNICIPIO_RES","TIPO_PACIENTE","FECHA_INGRESO","FECHA_SINTOMAS","FECHA_DEF","INTUBADO","NEUMONIA","EDAD","NACIONALIDAD","EMBARAZO","HABLA_LENGUA_INDIG","INDIGENA","DIABETES","EPOC","ASMA","INMUSUPR","HIPERTENSION","OTRA_COM","CARDIOVASCULAR","OBESIDAD","RENAL_CRONICA","TABAQUISMO","OTRO_CASO","TOMA_MUESTRA","RESULTADO_LAB","CLASIFICACION_FINAL","MIGRANTE","PAIS_NACIONALIDAD","PAIS_ORIGEN","UCI"
2020-10-12,1c4583,2,12,09,2,09,09,004,1,2020-03-30,2020-03-30,9999-99-99,97,2,23,1,97,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,99,México,97,97
2020-10-12,0d55c9,2,12,09,1,09,09,016,1,2020-03-26,2020-03-24,9999-99-99,97,2,28,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,3,99,México,97,97
...
```
Generar el archivo en formato JSON con la siguiente estructura (la estructura, nosotros la definimos):
```json
[
    {
        "FECHA_ACTUALIZACION": "2020-10-12",
        "ID_REGISTRO": "1c4583",
        "ORIGEN": "2",
        "SECTOR": "12",
        "ENTIDAD_UM": "09",
        "SEXO": "2",
        "ENTIDAD_NAC": "09",
        "ENTIDAD_RES": "09",
...
        "RESULTADO_LAB": "1",
        "CLASIFICACION_FINAL": "3",
        "MIGRANTE": "99",
        "PAIS_NACIONALIDAD": "M\u00c3\u00a9xico",
        "PAIS_ORIGEN": "97",
        "UCI": "97"
    },
    {
        "FECHA_ACTUALIZACION": "2020-10-12",
        "ID_REGISTRO": "0d55c9",
        "ORIGEN": "2",
        "SECTOR": "12",
        "ENTIDAD_UM": "09",
...
]
```
Donde las llaves de los objetos son los nombres de las columnas obtenidos del primer registro del archivo.

---
**ACTIVIDAD**: Crea el script `csvtojson.py NOMBRE` que lea el contenido de un archivo de texto en formato CSV y lo transforme a un archivos en formato JSON.

```sh
$ python csvtojson.py  --latin-1 datos/covid19-cdmx.csv
Conversión terminada, se ha creado el archivo datos/covid19-cdmx.json

$
```

---
**RETO**: Crea el script `jsontocsv.py NOMBRE` que lea el contenido de un archivo de texto en formato JSON y lo transforme a un archivos en formato CSV.

Notas:
- Se seugiere usar el archivo creado en la actividad anterior, así que tu objetivo es obtener el archivo `covid19-cdmx.csv` por lo que sería bueno que el original lo renombres a `covid19-cdmx.1.csv` para que puedas comprobar tus resultados.
- El primer registro del archivo CSV tiene que ser la lista de los nombres de las columnas, recuerda que si tienes un diccionario puedes usar la función `mi_diccionario.keys()`.
- Para guardar tus registros en formato CSV puedes usar la función `mi_arch_csv.writerow(-lista de campos-)` o `mi_arch_csv.writerows(-lista de registros-)`


```sh
$ python jsontocsv.py --latin-1 datos/covid19-cdmx.json
Conversión terminada, se ha creado el archivo datos/covid19-cdmx.csv

$
```
Compara tus resultados con el archivo original.

---
**SUPER-RETO**: Que pasaría si el archivo original en formato CSV o JSON fueran muy grandes que no se puedan procesar sólo en memoria. ¿Habría alguna forma en que se pueda procesar de forma más óptima la conversiones no importando si el archivo tiene 1KByte o 1TByte?

Modifica uno o ambos scripts creados con anterioridad para hacer uso eficiente de la memoria.
