print("Entrer une phrase pour compter les voyelles:")
sentence = input()
count = 0
for letter in sentence:
    if letter.lower() in [
        "a", "e", "i", "o", "u", "y", 
        "à", "â", "ä", "à", 
        "é", "è", "ê", "ë", 
        "ö", "ô", "ò",
        "ù", "û", "ü", "ù",
        "ÿ"
    ]:
        count +=1

print(f"il y a {count} voyelle dans la phrase donnée.")