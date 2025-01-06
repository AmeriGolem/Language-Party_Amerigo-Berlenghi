from function_def import rand_generator, get_number

gen_number = rand_generator("seed", a=1, b=1000)[0]

print("deviner le nombre en 10 essaies.")
tours = 0

for turn in range(10):
    print(f"il reste {10-turn} essaies.")
    guess = get_number("int")
    if guess == gen_number:
        tours = turn + 1
        break
    elif guess > gen_number:
        print (f"Le nombre à deviner est plus petit que {guess}.")
    elif guess < gen_number:
        print (f"Le nombre à deviner est plus grand que {guess}.")
    else:
        print("il y a eu une erreur")

print(f"Félicitation, vous avez deviner le nombre en {tours} essaies\nLe nombre était {gen_number}")