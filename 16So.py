points = {"Gryffindor": 0,"Ravenclaw": 0,"Hufflepuff": 0,"Slytherin": 0}

# Pregunta 1
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer1 = int(input("Enter your choice (1 or 2): "))
if answer1 == 1:
    points["Gryffindor"] += 1
    points["Ravenclaw"] += 1
elif answer1 == 2:
    points["Hufflepuff"] += 1
    points["Slytherin"] += 1
else:
    print("Entrada incorrecta")

# Pregunta 2
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer2 = int(input("Enter your choice (1-4): "))
if answer2 == 1:
    points["Hufflepuff"] += 2
elif answer2 == 2:
    points["Slytherin"] += 2
elif answer2 == 3:
    points["Ravenclaw"] += 2
elif answer2 == 4:
    points["Gryffindor"] += 2
else:
    print("Entrada incorrecta")

# Pregunta 3
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer3 = int(input("Enter your choice (1-4): "))
if answer3 == 1:
    points["Slytherin"] += 4
elif answer3 == 2:
    points["Hufflepuff"] += 4
elif answer3 == 3:
    points["Ravenclaw"] += 4
elif answer3 == 4:
    points["Gryffindor"] += 4
else:
    print("Entrada incorrecta")

print("\nPuntuaciones finales:")
for house, score in points.items():
    print(f"{house}: {score}")