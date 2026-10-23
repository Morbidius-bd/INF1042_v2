import random

options = ["pierre", "feuille", "ciseaux"]

choix = random.choice(options)
choix_utilisateur = random.choice(choix)

if choix == choix_utilisateur:
  print("Égalité")

else:
  print("Choix différents")
  
