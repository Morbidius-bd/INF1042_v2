mots = ["chat", "chien", "chat", "oiseau", "chien", "chat"]
freq = {}

for m in mots:
  freq[m] = freq.get(m, 0) + 1
print(freq)
