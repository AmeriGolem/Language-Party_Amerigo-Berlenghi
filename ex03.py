from function_def import get_number

print("Choix de température Celsius à convertir:")
temp = get_number()
Fahrenheit = (temp * 9/5) + 32

print(f"{temp} °C est convertie en {Fahrenheit} °F.")