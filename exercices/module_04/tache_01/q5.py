texte = input("Enterz une phrase: ")

vowels = "aeiouy"
nb_voyelles = 0

for letter in texte:
  if letter.lower() in vowels:
    nb_voyelles += 1

print(f"Nombre total de voyelles : {nb_voyelles}")
  
