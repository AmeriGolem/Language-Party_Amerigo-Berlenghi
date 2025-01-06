from function_def import get_number, rand_generator

print("Quel est la longueur du mot de passe souhaité ?")
length = get_number("int")

numbers = rand_generator("seed", length,33,126)
password = ""
for number in numbers:
    password += chr(number)
print(password)