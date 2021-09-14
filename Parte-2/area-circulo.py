# 1. leer el rádio desde la entrada estándar
# 2. calcular el área
# 3. imprimir el resultado
PI = 3.14159

radio_str = input("Dame el radio: ")
radio = float(radio_str)
area = PI * radio ** 2
print("El área del círculo es: " + str(area))
