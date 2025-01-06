from function_def import get_number

print("quel opération voulez-vous faire? veuillez choisir entre: +, -, *, /")
operation = input()
while operation not in ["+","-","*","/"]:
    print("Vous n'avez pas choisis une opération valide.")
    print("quel opération voulez-vous faire? veuillez choisir entre: +, -, *, /")
    operation = input()

print("choix du premier nombre:")
nombre_1 = get_number()
print("choix du deuxième nombre:")
nombre_2 = get_number()

if operation == "+":
    output = nombre_1 + nombre_2
elif operation == "-":
    output = nombre_1 - nombre_2
elif operation == "*":
    output = nombre_1 * nombre_2
elif operation == "/":
    output = nombre_1 / nombre_2

print(f"le résultat est: {output}")