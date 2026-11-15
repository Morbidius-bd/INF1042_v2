with open('exercices/module_4/tâche_02/valeurs.txt', 'r', encoding='utf-8') as f:
    contenu = f.readlines()

nombres = [int(ligne.strip()) for ligne in contenu]

valeur_max = max(nombres)
valeur_min = min(nombres)
moyenne = sum(nombres) / len(nombres)

print("Valeur_max :", valeur_max)
print("Valeur_min :", valeur_min)
print("Moyenne :", moyenne)
