import random

options = ["pierre", "feuille", "ciseaux"]

choix = random.choice(options)
choix_utilisateur = input("Entrez votre choix: Pierre, Feuille ou Ciseaux:")

if choix == choix_utilisateur:
  print("Égalité")

else:
  print("Choix différents")
  
