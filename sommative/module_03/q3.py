Afficher : montant initial, pourcentage de rabais, montant économisé, sous-total après rabais, taxe et total final.
Afficher tous les montants avec 2 décimales.
   pour un achat de 120 $, appliquer d’abord 10 % de rabais, puis calculer la taxe sur le montant réduit.


montant_sans_taxes = float(input("Quel est le montant payé?:"))
if montant_sans_taxes < 50:
  rabais = montant_sans_taxes * 0
  print("Aucun rabais")
elif montant_sans_taxes >= 50 and montant_sans_taxes <= 100:
  rabais = montant_sans_taxes * 0.05
  print(f"Votre rabais est de {rabais}:.2f")
else:
  rabais = montant_sans_taxes * 0.1
  print(f"Votre rabais est de {rabais}:.2f")
  
sous_total = montant_sans_taxes - rabais
taxes = sous_total * 0.13
montant_restant = sous total - taxe 

print(f"Pour un achat de {montant_sans_taxes}, appliquer un rabais de 


                                
