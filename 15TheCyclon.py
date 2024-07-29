height = int(input("¿Cuál es tu altura en centímetros? "))
credits = int(input("¿Cuántos créditos tienes? "))

height_required = 140
credits_required = 50

if height >= height_required and credits >= credits_required:
    print("¡Disfruta el viaje!")
elif credits >= credits_required:
    print("No eres lo suficientemente alto para viajar.")
elif height >= height_required:
    print("No tienes suficientes créditos.")
else:
    print("No cumples con ninguno de los requisitos.")   