 matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
    ("Tigres", "Panthères", 25, 23),
    ("Lynx", "Aigles", 19, 25),
    ("Tigres", "Aigles", 21, 25),
    ("Lynx", "Panthères", 25, 20),
)

# 1. Récupérer toutes les équipes et initialiser leurs statistiques
equipes = {eq for eq1, eq2, _, _ in matchs for eq in (eq1, eq2)}
stats = {eq: {"victoires": 0, "defaites": 0, "points": 0} for eq in equipes}

# 2. Analyser chaque match et afficher le gagnant
print("--- Résultats des matchs ---")
for eq1, eq2, score1, score2 in matchs:
    stats[eq1]["points"] += score1
    stats[eq2]["points"] += score2

    if score1 > score2:
        stats[eq1]["victoires"] += 1
        stats[eq2]["defaites"] += 1
        print(f"Les {eq1} ont battu les {eq2} par {score1} à {score2}.")
    elif score2 > score1:
        stats[eq2]["victoires"] += 1
        stats[eq1]["defaites"] += 1
        print(f"Les {eq2} ont battu les {eq1} par {score2} à {score1}.")
    else:
        print(f"Match nul entre les {eq1} et les {eq2} ({score1} à {score2}).")

# 3. Victoires, points totaux et bilan victoires/défaites par équipe
print("\n--- Bilan par équipe ---")
for eq, s in stats.items():
    v, d, p = s["victoires"], s["defaites"], s["points"]
    if v > d:
        bilan = "plus de victoires que de défaites"
    elif v < d:
        bilan = "plus de défaites que de victoires"
    else:
        bilan = "autant de victoires que de défaites"

    print(f"{eq} : {v} victoire(s), {p} point(s) — a terminé avec {bilan}.")

# 4. Meilleure équipe en victoires et en points
plus_victoires = max(stats, key=lambda eq: stats[eq]["victoires"])
plus_points = max(stats, key=lambda eq: stats[eq]["points"])

print("\n--- Champions du tournoi ---")
print(f"Plus de victoires : {plus_victoires} ({stats[plus_victoires]['victoires']} victoires)")
print(f"Plus de points : {plus_points} ({stats[plus_points]['points']} points)")
