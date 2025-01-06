print("quel opération voulez-vous faire? veuillez choisir entre: +, -, *, /")
operation = input()
while operation not in ["+","-","*","/"]:
    print("Vous n'avez pas choisis une opération valide.")
    print("quel opération voulez-vous faire? veuillez choisir entre: +, -, *, /")
    operation = input()

def get_number()-> int:
    while True:
        print("Veuillez choisir un nombre")
        nombre_str = input()
        try:
            nombre_float = float(nombre_str)
            break
        except ValueError:
            print(f"Votre choix n'est pas valide.")
    return nombre_float

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