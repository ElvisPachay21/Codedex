import random

def get_random_answer():
    return random.choice(["Sí", "No"])

input("Hazme una pregunta: ")
print(get_random_answer())