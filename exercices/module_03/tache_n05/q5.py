age = int(input("Entrez votre age:"))

if age < 13:
  print("Enfant")
elif age >= 13 and age <= 17:
  print("Adolescent")
elif age >= 18 and age <= 64:
  print("Adulte")
else:
  print("Aîné")
