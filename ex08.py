from function_def import get_number

number_list = []
print("Premier nombre:")
number_list.append(get_number())
print("deuxième nombre:")
number_list.append(get_number())
print("Troisème nombre:")
number_list.append(get_number())

max_number = max(number_list)

print(f"Le nombre le plus grand qui a été donné est {max_number}.")