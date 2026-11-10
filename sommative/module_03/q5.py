import random

victoires = 0
défaites = 0
égalités = 0

user_choice = int(input("Choisissez entre pierre, feuille et ciseaux:"))
print(f"{user_choice} a été choisit par l'utilisateur")

if user_choice == quitter:
  break
elif user_choice != quitter and user_choice != ["pierre", "feuille", "ciseaux"]:
  print("Choix invalide")
else:
  choice = [pierre, feuille, ciseaux]

computer_choice = random.choice
print(f"{computer_choice} a été choisit par  l'ordinateur")

if user_choice == pierre and computer_choice == ciseaux:
  print("L'utilisateur a gagné!")
  victoires += 1
elif user_choice == feuille and computer_choice == pierre:
  print("L'utilisateur a gagné!")
  victoires += 1
elif user_choice == ciseaux and computer-choice == feuille:
  print("L'utilisateur a gagné!")
  victoires += 1
elif user_choice == computer_choice:
  print("Égalité")
  égalités += 1
else:
  print("L'ordinateur a gagné!")
  défaites += 1

print(f" Vous possedez {victoires} victoires, {défaites} défaites et {égalités} égalités contre l'ordinateur")
