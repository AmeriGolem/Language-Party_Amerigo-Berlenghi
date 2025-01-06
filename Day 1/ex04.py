from function_def import get_number

number = get_number("int")
print(f"table de multiplication de {number}")
for i in range(10):
    print(f"{i+1} x {number} = {number * (i+1)}")