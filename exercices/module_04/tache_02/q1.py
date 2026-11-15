import random

with open("exercices/module_4/tâche_02/valeurs.txt", "w", encoding="utf-8") as fichier:
    for _ in range(1000):
        nombre = random.randint(0, 100000)
        fichier.write(f"{nombre}\n")

