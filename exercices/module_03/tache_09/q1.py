import secrets
import string

nom = input("Entrez votre prenom:")
prenom = input("Entrer votre nom:")
annee_de_naissance = int(input("Entrez votre annee de naissance:"))
ville = input("Ville de naissance:")

identifiant = f"{prenom}.{nom}@{ville}.ca"
print(f"identifiant généré: {identifiant}")

mot_de_passe = secrets.choice(string.ascii_letters + string.digits)

for i in range(4):
    mot_aleatoire = "".join(mot_de_passe) 
    print(mot_aleatoire) 
