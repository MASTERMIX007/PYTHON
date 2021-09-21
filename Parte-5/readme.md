## Parte 5 – Manejo de Datos

- Archivos de texto
- Archivos de texto estructurados (CSV)
- Archivos binarios estructurados
- Introducción a almacenamiento de datos NoSQL (JSON)
- Bases de datos relacionales (SQL)
- Programas y Procesos

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

Uno de los archivos de texto estructurados que lleva años siendo usado son los archivos CSV (Comma Separator Values) y que pueden ser exportados o leídos por una multitud de sistemas, plataformas o programas, así que conviene conocer como manejar este tipo de formato desde Python.

Estos archivos como ya se mencinó son archivos de texto, que representan información de forma tabular, así que cada línea representa un registro o fila de la tabla y este registro contiene generalmente columnas o valores que están relacionadas entre sí ya que representan propiedades de la misma entidad. Por ejemplo una fila podría representar un estado de la república mexicana y cada valor o columna represntario datos como nombre de estado, población, producto interno bruto, indice de natalidad, etc.

Ejemplo:
```csv
id,name,Gender,Race,Alignment
0,A-Bomb,Male,Human,good
1,Abe Sapien,Male,Icthyo Sapien,good
2,Abin Sur,Male,Ungaran,good
3,Abomination,Male,Human / Radiation,bad
4,Abraxas,Male,Cosmic Entity,bad
5,Absorbing Man,Male,Human,bad
6,Adam Monroe,Male,-,good
7,Adam Strange,Male,Human,good
8,Agent 13,Female,-,good
9,Agent Bob,Male,Human,good
10,Agent Zero,Male,-,good
```

Aunque estos archivos los podría leer y escribir usando las herramientas básicas de Python, hay una forma más simple y es usando el paquete `csv` que es parte de la librería estándar de Python.

La documentación se puede consultar es: https://docs.python.org/3/library/csv.html

Vamos a ver como funciona el módulo `csv` realizando algunas prácticas desde IPython leyendo los datos del archivo `datos/heroes_information-10.csv`:

```python
In [50]: import csv

In [51]: with open("datos/heroes_information-10.csv", "r") as arch_txt:
    ...:     reader_csv = csv.reader(arch_txt)
    ...:     datos_list = list( reader_csv )
    ...: 

In [52]: datos_list
Out[52]: 
[['id', 'name', 'Gender', 'Race', 'Alignment'],
 ['0', 'A-Bomb', 'Male', 'Human', 'good'],
 ['1', 'Abe Sapien', 'Male', 'Icthyo Sapien', 'good'],
 ['2', 'Abin Sur', 'Male', 'Ungaran', 'good'],
 ['3', 'Abomination', 'Male', 'Human / Radiation', 'bad'],
 ['4', 'Abraxas', 'Male', 'Cosmic Entity', 'bad'],
 ['5', 'Absorbing Man', 'Male', 'Human', 'bad'],
 ['6', 'Adam Monroe', 'Male', '-', 'good'],
 ['7', 'Adam Strange', 'Male', 'Human', 'good'],
 ['8', 'Agent 13', 'Female', '-', 'good'],
 ['9', 'Agent Bob', 'Male', 'Human', 'good'],
 ['10', 'Agent Zero', 'Male', '-', 'good']]

In [53]: 
```

**Notas:**
1. El resultado de leer un archivo CSV es una lista de sublistas, donde cada sublista representa una fila.
2. Algunos archivos pueden contener una primera fila con las etiquetas de las columnas y no forman parte de los datos, en este caso si existe y deberá ignorarse por siblemente creando una sublista con `datos_list[1:]`
3. Todas las filas o las sublistas, tiene siempre la misma cantidad de elementos, aunque algunos estén vacios o con valores representando nulos.
4. Todos los datos leídos de un archivo CSV son de tipo texto, así que si se necesita una columna en algún tipo diferente habrá que convertirla.

Ahora vamos a eliminar el Superheroe `Adam Monroe` y luego agregar a "Hulk" con lo datos "Male", "Human / Radiation", "good":

```python
In [53]: datos_list[7]
Out[53]: ['6', 'Adam Monroe', 'Male', '-', 'good']

In [54]: del( datos_list[7] )

In [55]: datos_list.append( ["11", "Hulk", "Male", "Human / Radiation", "good"]
    ...: )

In [56]: datos_list
Out[56]: 
[['id', 'name', 'Gender', 'Race', 'Alignment'],
 ['0', 'A-Bomb', 'Male', 'Human', 'good'],
 ['1', 'Abe Sapien', 'Male', 'Icthyo Sapien', 'good'],
 ['2', 'Abin Sur', 'Male', 'Ungaran', 'good'],
 ['3', 'Abomination', 'Male', 'Human / Radiation', 'bad'],
 ['4', 'Abraxas', 'Male', 'Cosmic Entity', 'bad'],
 ['5', 'Absorbing Man', 'Male', 'Human', 'bad'],
 ['7', 'Adam Strange', 'Male', 'Human', 'good'],
 ['8', 'Agent 13', 'Female', '-', 'good'],
 ['9', 'Agent Bob', 'Male', 'Human', 'good'],
 ['10', 'Agent Zero', 'Male', '-', 'good'],
 ['11', 'Hulk', 'Male', 'Human / Radiation', 'good']]

In [57]: 
```

**Notas:** La forma de eliminar y agregar información es sólo una forma de hacerlo, dependerá de como estén estructurados los datos.

Ahora vamos a guardar la información en el archivo `heroes-10.csv`, luego abre el archivo con Sublime Text y corrobora la información, también podrías abrir el archivo con una hoja de cálculo como Libre Calc o Google Sheet o Excel y corrobora la información.

```python
In [57]: with open("datos/heroes-10.csv", "w", newline="") as escritor_txt:
    ...:     writer_csv = csv.writer(escritor_txt)
    ...:     writer_csv.writerows(datos_list)
    ...: 

In [58]: cat datos/heroes-10.csv
id,name,Gender,Race,Alignment
0,A-Bomb,Male,Human,good
1,Abe Sapien,Male,Icthyo Sapien,good
2,Abin Sur,Male,Ungaran,good
3,Abomination,Male,Human / Radiation,bad
4,Abraxas,Male,Cosmic Entity,bad
5,Absorbing Man,Male,Human,bad
7,Adam Strange,Male,Human,good
8,Agent 13,Female,-,good
9,Agent Bob,Male,Human,good
10,Agent Zero,Male,-,good
11,Hulk,Male,Human / Radiation,good

In [59]: 
```

---
**Ejemplo:** Vamos a modificar el script `lss.py` para agregar la función `imprime_csv()` que imprima la lista de archivos en la salida estándar en formato CSV haciendo uso de la opción `--csv`

Ejemplo de ejecución:
```sh
$ ./lss.py --csv
./lss.py,1759,21-09-2021
./lss-rt.py,2052,21-09-2021
./readme.md,23726,21-09-2021
./datos,4096,21-09-2021
./imprime_passwd.py,751,21-09-2021
./.ipynb_checkpoints,4096,21-09-2021
```

También se podría redireccionar la salidar estándar a un archivo y luego abrir éste archivo con alguna hoja de cálculo.

**Ejemplo:** Crear el script `grep-csv.py [N:TEXTO] ARCHIVO` para que realice:
1. Imprima en la salida estándar las líneas de ARCHIVO
2. Sólo imprime las filas cuya columna N coincida con texto
3. Si la columna N y el TEXTO no se proporcionan, entonces se imprimen todas las filas.

Ejemplo de ejecución:
```sh
$ ./grep-csv-rt.py datos/Base\ Datos\ xls\ -\ 14\ Sep.\ 2021\,\ 00\ Hs.\ 52\ min.csv HOSPITALMUJER
2646,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '2646',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2670,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2671,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2672,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2673,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2674,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2675,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2676,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2677,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2678,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
2679,Troncal sip2,Issabel,HOSPITALMUJER,HMEMN '_267[0-9]',10.200.51.2,"14 Sep. 2021, 00 Hs. 52 min"
```

**Ejemplo/Ejercicio:** Modifica el script `grep-csv.py [N:TEXTO] ARCHIVO` para que realice una operación definida por los alumnos.


### Archivos binarios estructurados

La mayoría de los archivos creados por aplicaciones que no son editores de código guardan la información en archivos binarios que tienen una estructura establecida por la organización creadora del software y puede ser una estructura con licencia abierta, donde todos pueden consultar un documento con la estructura o pueder ser privativo, donde sólo la empresa y quienes tengan autorizado conocen el formato de estos archivos.

Un caso muy usado son los archivos con extensión `.xlsx` que genera la aplicación Excel y que un formato binario para almacenar hojas de cálculo.

Para poder abrir, leer, escribir o modoficar archivos binarios se necesita de encontrar el módulo adecuado que permita manipular los datos binarios, o en su caso, si no existe será necesario crearlo, ya sea siguiendo alguna documentación o mediante ingeniería inversa.

Por ejemplo, para poder abrir y leer la información en el archivo `datos/Base Datos xls - 14 Sep. 2021, 00 Hs. 52 min.xlsx` será necesario hacer uso del paquete `openpyxl` que no es parte de la librería estándar, por lo tanto es necesario realizar la instalación con el comando:

```sh
$ pip install openpyxl
Collecting openpyxl
  Downloading openpyxl-3.0.8-py2.py3-none-any.whl (244 kB)
     |████████████████████████████████| 244 kB 238 kB/s 
Collecting et-xmlfile
  Using cached et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-1.1.0 openpyxl-3.0.8
```

**Ejemplo:** Crear el script `cat-xlsx.py ARCHIVO` que imprime el contenido de ARCHIVO en formato binario XLSX.

Ejemplo de salida:
```sh
$ ./cat-xlsx-rt.py datos/Base\ Datos\ xls\ -\ 14\ Sep.\ 2021\,\ 00\ Hs.\ 52\ min.xlsx
DID   TIPO                      Modelo                      UNIDAD                                              PARTITION/RUTA SALIDA                                    IP PBX         REGISTRO                   
1000  extensiones sip2                                      RESERVADA                                                                                                                                              
1001  extensiones sip2                                      MESA DE ENTRADA CECOM                                                                                                                                  
1002  Troncal sip2              Issabel                     HMR_XII_RM                                          HMR_XIIRM '_100[2-4]'                                    10.45.135.5    14 Sep. 2021, 00 Hs. 52 min
1003  Troncal sip2              Issabel                     HMR_XII_RM                                          HMR_XIIRM '_100[2-4]'                                    10.45.135.5    14 Sep. 2021, 00 Hs. 52 min
1004  Troncal sip2              Issabel                     HMR_XII_RM                                          HMR_XIIRM '_100[2-4]'                                    10.45.135.5    14 Sep. 2021, 00 Hs. 52 min
1005  Troncal sip2              Elastix                     a_SIP_ESG                                           ESC_SUP_GRRA '_100[5-8]'                                 10.7.168.3     14 Sep. 2021, 00 Hs. 52 min
1006  Troncal sip2              Elastix                     a_SIP_ESG                                           ESC_SUP_GRRA '_100[5-8]'                                 10.7.168.3     14 Sep. 2021, 00 Hs. 52 min
1007  Troncal sip2              Elastix                     a_SIP_ESG                                           ESC_SUP_GRRA '_100[5-8]'                                 10.7.168.3     14 Sep. 2021, 00 Hs. 52 min
1008  Troncal sip2              Elastix                     a_SIP_ESG                                           ESC_SUP_GRRA '_100[5-8]'                  
```

Con la información contenida en una lista de sublistas es posible procesar la información como si de un archivo csv se tratara.


### Introducción a almacenamiento de datos NoSQL (JSON)

Hasta el momento hemos estado manejando archivos de tipo texto plano o archivos en formato CSV que también son archivos de texto, pero que siguen ciertas reglas o estructura, ahora vamos a revisar otro tipo de formato de archivos de texto conocido como JSON y que también es muy usado para el intercambio de información.

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

---
**Ejemplo:** Crea el script `lee-json.py NOMBRE` para que lea el contenido del archivo NOMBRE en formato JSON y lo imprima en la salida estándar.

```sh
$ python lee-json.py datos/anime.json
Usage: lee-json.py [OPTIONS] NOMBRE

  Lee el contenido de NOMBRE en formato JSON y lo imprime en la salida
  estándar

Options:
  --help  Show this message and exit.

$ ./lee-json.py anime.json 
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

---
**Ejemplo:** Crea el script `anime-json.py` para que lea el contenido del archivo `anime.json` e imprima en la salida estándar el `id`, `título` y `link poster original`

```sh
$ ./anime-json.py
id: 1
titulo: Cowboy Bebop
Poster original: https://media.kitsu.io/anime/poster_images/1/original.jpg?1431697256
```

Y como actividad adicional, podrías abrir el link a la imagen para ver el poster!

---
**Ejercicio:** Modifica el script `anime-json.py` para que incluya el link de la portada original.

```sh
$ ./anime-json.py
id: 1
titulo: Cowboy Bebop
Poster original: https://media.kitsu.io/anime/poster_images/1/original.jpg?1431697256
Portada original: https://media.kitsu.io/anime/cover_images/1/original.jpg?1416336000
```

Y como actividad adicional, podrías abrir el link a la imagen para ver la portada!

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
**Ejemplo:** Crea el script `csvtojson.py NOMBRE` que lea el contenido de un archivo de texto en formato CSV y lo transforme a un archivos en formato JSON.

```sh
$ python csvtojson.py  --latin-1 datos/covid19-cdmx.csv
Conversión terminada, se ha creado el archivo datos/covid19-cdmx.json

$
```

---
**Ejercicio:** Crea el script `jsontocsv.py NOMBRE` que lea el contenido de un archivo de texto en formato JSON y lo transforme a un archivos en formato CSV.

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

