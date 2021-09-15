#!/usr/bin/env python
# -*- coding: utf-8 -*-

superheroe = {
      "name": "Iron Man",
      "realname": "Tony Stark",
      "team": "Avengers",
      "firstappearance": "1963",
      "createdby": "Stan Lee",
      "publisher": "Marvel Comics",
      "imageurl": "https://www.simplifiedcoding.net/demos/marvel/ironman.jpg",
      "bio": "\r\n\t\tAnthony Edward Stark, the son of wealthy industrialist and head of Stark Industries, Howard Stark, and Maria Stark. A boy genius, he enters MIT at the age of 15 to study electrical engineering and later receives master's degrees in electrical engineering and physics. After his parents are killed in a car accident, he inherits his father's company.\r\n\t\t"
}

# Tu código aquí
llave = "name"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "realname"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "team"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "firstappearance"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "createdby"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "publisher"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "imageurl"
valor = superheroe[llave]
print(f"{llave.title():16} | {valor:40}")
llave = "bio"
valor = superheroe[llave]
print(f"{llave.title()}:")
print(f"{valor:59}")