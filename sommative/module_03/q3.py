montant_sans_taxes = float(input("Quel est le montant payé?:")) 

if montant_sans_taxes < 50:
  pourcentage_rabais = 0
elif montant_sans_taxes >= 50 and montant_sans_taxes <= 100:
  pourcentage_rabais = 5
else:
  pourcentage_rabais = 10
  
montant_economise = montant_initial * (pourcentage_rabais / 100)
sous_total = montant_sans_taxes - montant_economise
taxes = sous_total * 0.13
total_final = sous_total + taxe

print(f"Montant initial : {montant_initial:.2f} $")
print(f"Pourcentage de rabais : {pourcentage_rabais} %")
print(f"Montant économisé : {montant_economise:.2f} $")
print(f"Sous-total après rabais : {sous_total:.2f} $")
print(f"Taxe (TVH 13%) : {taxe:.2f} $")
print(f"Total final : {total_final:.2f} $")


                                
