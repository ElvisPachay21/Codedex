import random

def magic_8_ball():
    respuestas = ["Sí.","No.","Tal vez.",]
    respuesta = random.choice(respuestas)
    
    return respuesta

if __name__ == "__main__":
    input("¡Haz tu pregunta! ")
    print(magic_8_ball())