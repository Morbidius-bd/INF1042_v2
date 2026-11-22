import random

liste = [random.randint(1, 20) for _ in range(100)]

nouvelle_liste = set(liste)
print(nouvelle_liste)
