# 1. leer el rádio desde la línea de comandos
# 2. calcular el área
# 3. imprimir el resultado
import sys

PI = 3.14159

# print(sys.argv)  # sys.argv es una lista
# print(sys.argv[0])
# print(sys.argv[1])

radio_str = sys.argv[1]
radio = float(radio_str)
area = PI * radio ** 2
print("El área del círculo es: " + str(area))
