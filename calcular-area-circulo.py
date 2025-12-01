import math

# Paso 1: Solicitar al usuario ingresar el radio del circulo

radio = float(input("Por favor ingrese el radio del circulo: "))

# Paso 2: Calcular area del circulo, utilizando la formula area = pi*radio^2

area = math.pi*(radio**2)  

# Paso 3: Mostrar area calculada
print("El area del circulo con radio",radio,"es:",area)