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