def calculer_prix_rabais(prix_initial, type_client):
    """
    Applique un rabais selon le statut du client :
    - 'VIP'     : 20% de réduction (0.20)
    - 'Membre'  : 10% de réduction (0.10)
    - 'Régulier': 0% de réduction (0.00)
    """
    if type_client == "VIP":
        rabais = prix_initial * 0.20
    elif type_client == "Membre":
        rabais = prix_initial * 0.10
    else:
        rabais = prix_initial * 0.00  # Corrigé : le rabais est de 0$, pas du prix entier

    prix_final = prix_initial - rabais
    return prix_final


def calculer_points_accumules(nombre_achats, points_par_achat):
    """
    Calcule le total de points pour un certain nombre d'achats effectués.
    Chaque achat accumule un montant fixe de points.
    """
    total_points = 0

    # Corrigé : range(0, nombre_achats) ou simplement range(nombre_achats) pour faire exactement N tours
    for i in range(nombre_achats):
        total_points += points_par_achat

    return total_points


def calculer_epargne_avec_bonus(montant_mensuel, nombre_mois):
    """
    Calcule le montant total épargné après un nombre de mois donné,
    en ajoutant un bonus fixe de 5$ chaque mois.
    """
    total = 0.0
    mois_actuel = 1

    # Corrigé : '<=' au lieu de '<' pour inclure le dernier mois
    while mois_actuel <= nombre_mois:
        total += (montant_mensuel + 5)  # Corrigé : '+=' au lieu de '=' pour accumuler les montants
        mois_actuel += 1

    return total


# --- EXÉCUTION DU TEST ---
if __name__ == "__main__":
    print("=== TEST 1 : Prix avec rabais VIP ===")
    prix_vip = calculer_prix_rabais(50.00, "VIP")
    print(f"Prix obtenu     : {prix_vip:.2f} $ (Attendu : 40.00 $)")

    print("\n=== TEST 2 : Points de fidélité (5 achats de 10 points) ===")
    points = calculer_points_accumules(nombre_achats=5, points_par_achat=10)
    print(f"Points obtenus  : {points} (Attendu : 50 points)")

    print("\n=== TEST 3 : Épargne sur 4 mois (50$ + 5$ bonus / mois) ===")
    epargne = calculer_epargne_avec_bonus(montant_mensuel=50.00, nombre_mois=4)
    print(f"Épargne obtenue : {epargne:.2f} $ (Attendu : 220.00 $)")
