temp_celsius = float(input("Entrez une valeur de temperature:"))
temp_fahrenheit = float(temp_celsius * 9 / 5) + 32
temp_kelvin = float(temp_celsius + 273.15)

if temp_celsius <= -273.15:
  print(f"Temperature non acceptable")
else:
  print(f"Votre temperature en celsius est de: {temp_celsius:.2f} celsius")
  print(f"Votre temperature en fahrenheit est: {temp_fahrenheit:.2f} fahrenheit")
  print(f"Votre temperature en kelvin est de: {temp_kelvin:.2f} kelvin")
