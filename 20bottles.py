num_bottles = 99

for i in range(num_bottles, 0, -1):
    if i > 1:
        print(f"{i} botellas de cerveza en la pared, {i} botellas de cerveza.")
        print("Toma una y pásala al compañero, {0} botellas de cerveza en la pared.\n".format(i - 1))
    else:
        print(f"{i} botella de cerveza en la pared, {i} botella de cerveza.")
        print("Toma una y pásala al compañero, ¡ya no hay más botellas de cerveza en la pared!\n")