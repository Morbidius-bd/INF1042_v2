moyenne = sum(float(notes)) / len(notes)
print(f"La moyenne est : {moyenne}")

for num in notes:
  highest_num = max(num, notes)
print(f"La valeur la plus fréquente est : {highest_num}")
