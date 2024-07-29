ph = float(input("Ingrese un valor de pH entre 0 y 14: "))
if ph < 0 or ph > 14:
    print("El valor ingresado está fuera del rango válido. Debe estar entre 0 y 14.")
else:
    if ph > 7:
        print("Básico")
    elif ph < 7:
        print("Ácido")
    else:
        print("Neutral")