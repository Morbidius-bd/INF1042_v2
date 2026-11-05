import time
import random

quiz = {
    "Quelle est la racine carre de 100 ?": "10",
    "Combien font 7 multiplié par 8 ?": "56",
    "Quel est le carre de 14 ?": "196",
    "Quelle est la valeur approximative de pi?": "3.14",
}

questions = list(quiz.keys())
random.shuffle(questions)

score = 0

print("--- Debut du quiz aleatoire ---")

temps_debut_global = time.time()

for question in questions:
  print(f"\nQuestion : {question}")
  reponse_utilisateur = input("Votre reponse:").strip

bonne_reponse = quiz[question]

if reponse_utilisateur.lower() == bonne_reponse.lower():
  print("Correct")
  score += 1
else:
  print(f"Incorrect. La bonne reponse etait: {bonne_reponse}")

temps_fin_global = time.time()

temps_total = temps_fin_global - temps_debut_global
temps_moyen = temps_total / len(questions)

print(f"\n--- Quiz terminé ! Votre score : {score}/{len(quiz)} ---")
print(f"Temps total mis : {temps_total:.2f} secondes")
print(f"Temps moyen par question : {temps_moyen:.2f} secondes")
