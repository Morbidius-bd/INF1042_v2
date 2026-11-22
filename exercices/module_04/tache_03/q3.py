import random

A = set(random.randint(1, 20))
B = set(random.randint(1, 20))

print("Union:", A | B)
print("Intersection:", A & B)
print("Différence:", A - B)


