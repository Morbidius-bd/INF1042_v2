nom = input("Entrer votre nom:")
if len(nom) >= 8 and len(nom) <= 12:
  print("Nom acceptable")
else:
  print("Erreur, nom trop court. Doit être entre 8 et 12 caractères")
