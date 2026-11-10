Demander à l’utilisateur d’entrer une température en Celsius.
Accepter les nombres entiers ou décimaux.
Calculer Fahrenheit avec : F = (C × 9 / 5) + 32.
Calculer Kelvin avec : K = C + 273.15.
Afficher les trois températures avec leur unité et arrondir les résultats à 2 décimales.
Refuser une température inférieure à -273.15 °C.

temp_celsius = input("Entrez une valeur de tempaerature:")
temp_fahrenheit = (temp_celsius * 9 / 5) + 32
temp_kelvin = temp_celsius + 273.15(round, 2)

if temp_celsius <= -273.15:
  print(f"Temperature non acceptable")
else:
  print(f"Votre temperature en celsius est de: {temp_celsius} celsius.:2f")
  print(f"Votre temperature en fahrenheit est: {temp_fahrenheit} fahrenheit.:2f")
  print(f"Votre temperature en kelvin est de: {temp_kelvin} kelvin.:2f")
