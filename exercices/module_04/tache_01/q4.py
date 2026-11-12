info = input("entrez un texte : ")

texte = info.lower()
list = info.split(",")

print(list)
combined = ' - '.join(list)

print(combined)
