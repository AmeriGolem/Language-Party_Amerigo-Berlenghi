from function_def import get_number

print("Donner un nombre pour calculer son factoriel:")
number = get_number("int")
result = 1
for n in range (1, number+1):
    result *= n
print(f"{number}! = {result}")