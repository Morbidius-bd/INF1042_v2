import secrets
import string

nom = input("Entrez votre prenom:")
prenom = input("Entrer votre nom:")
annee_de_naissance = int(input("Entrez votre annee de naissance:"))
ville = input("Ville de naissance:")

identifiant = string({prenom}.{nom}@{ville}.ca)
print(identifiant)
# Générer une liste de 5 lettres aléatoires
mot_de_passe = secrets.choices(string.ascii_letters + string.digits, k=4)

# Pour obtenir une chaîne de caractères plutôt qu'une liste :
mot_aleatoire = "".join(mot_de_passe)
print(mot_aleatoire)  # Exemple : 'xKzLp'
