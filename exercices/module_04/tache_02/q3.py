with open('exercices/module_4/tâche_02/valeurs.txt', 'r', encoding='utf-8') as f:
    contenu = f.readlines()

nombres = [int(ligne.strip()) for ligne in contenu]

with open('exercices/module_4/tâche_02/petites_valeurs.txt', 'w', encoding='utf-8') as f_out:
    for nombre in nombres:
        if 0 <= nombre <= 49999:
            f_out.write(f"{nombre}\n")
          
with open('exercices/modules_4/tâche_02/haut.txt', 'w', encoding='utf-8') as f_in:
  for nombre in nombres:
    if 50000 <= nombre <= 100000:
      f_in.write(f"{nombre}\n")
