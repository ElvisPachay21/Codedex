import random

numero_a_adivinar = random.randint(1, 100)
intentos_maximos = 5
tries = 0

print("Adivina el número entre 1 y 100")

while tries < intentos_maximos:
    try:
        guess = int(input("Introduce tu adivinanza: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if guess < numero_a_adivinar:
        print("El número es mayor.")
    elif guess > numero_a_adivinar:
        print("El número es menor.")
    else:
        print("¡Felicidades! ¡Adivinaste el número!")
        break

    tries += 1 

if tries == intentos_maximos and guess != numero_a_adivinar:
    print(f"Lo siento, se te han acabado los intentos. El número era {numero_a_adivinar}.")