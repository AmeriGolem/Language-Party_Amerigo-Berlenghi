print("Veuillez insérer un mot pour que le programme puisse vérifier si c'est un palindrome.")
word = input()
drow = word[::-1]
if word == drow:
    print(f"le mot {word} est un palindrome.")
else:
    print(f"le mot {word} n'est pas un palindrome.")