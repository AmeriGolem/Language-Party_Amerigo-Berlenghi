from function_def import get_number, rand_generator

random_number = rand_generator("seed", a=1, b=100)[0]
guessed = False
attempts = 0

while not guessed:
    print("Choisissez un nombre à deviner:")
    guess = get_number("int")
    if guess == random_number:
        guessed = True
    elif guess > random_number:
        print (f"Le nombre à deviner est plus petit que {guess}.")
    elif guess < random_number:
        print (f"Le nombre à deviner est plus grand que {guess}.")
    else:
        print("il y a eu une erreur")
    attempts += 1

print(f"Bravo le nombre à deviner était {random_number}, vous avez prit {attempts} essaies.")