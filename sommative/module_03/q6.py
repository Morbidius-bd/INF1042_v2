import math


reponse_elec = input("Le véhicule est-il électrique ? (oui/non) : ").strip().lower()
est_electrique = reponse_elec in ["oui", "yes"]


duree = float(input("Entrez le nombre d'heures de stationnement : "))


heures_facturees = math.ceil(duree)

if heures_facturees <= 0:
    prix_brut = 0.0
else:
    
    prix_brut = 4.00 + (heures_facturees - 1) * 2.50
    
    prix_brut = min(prix_brut, 20.00)


if est_electrique:
    rabais = prix_brut * 0.20
else:
    rabais = 0.0

total_final = prix_brut - rabais

print("--- DÉTAILS DE LA FACTURATION ---")
print(f"Durée exacte : {duree} h")
print(f"Heures facturées : {heures_facturees} h")
print(f"Prix avant rabais : {prix_brut:.2f} $")
print(f"Rabais : {rabais:.2f} $")
print(f"Total final : {total_final:.2f} $")

  



  
