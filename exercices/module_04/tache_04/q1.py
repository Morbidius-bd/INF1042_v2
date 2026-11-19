notes = [12, 15, 9, 18, 15, 12]

moyenne = sum(float(notes)) / len(notes)
print(f"La moyenne est : {moyenne}")

  highest_num = max(notes, key=notes.count)
print(f"La valeur la plus fréquente est : {highest_num}")
