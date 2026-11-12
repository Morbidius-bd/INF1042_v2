texte = input("Enterz une phrase: ")

vowels = "aeiouy"
nb_vowels = 0

for letter in texte:
  if letter.lower() in vowels:
    nb_vowels += 1

print(f"Nombre total de voyelles : {nb_voyelles}")
  
