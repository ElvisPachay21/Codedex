import math

a = float(input("Introduce el valor del cateto a: "))
b = float(input("Introduce el valor del cateto b: "))

c = math.sqrt(a**2 + b**2)

print(f"La hipotenusa es: {c:.2f}")