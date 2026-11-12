import random

tirages = int(input("Combien de tirage souhaiter vous effectuer?:"))

compteurs = {1: 0, 2: 0, 3: 0, 4: 0}

for _ in range(tirages):
  resultats = random.randint(1, 4)
  compteurs[resultats] += 1

print("\n--- RÉSULTATS ---")

for valeur, nombre in compteurs.items():
  pourcentage = (nombre / tirages) * 100
  print(f"Nombre {valeur}: {nombre} fois ({pourcentage:.2f})")

plus_frequent = max(compteurs, key=compteurs.get)
print(f"Le nombre tiré le plus souvent est le {plus_frequent} ({compteurs[plus_frequent]} tirages).")
  
