list_of_numbers = []
for number in range(1, 101):
    if (number%3 == 0) & (number%5 == 0):
        list_of_numbers.append("FizzBuzz")
    elif number%3 == 0:
        list_of_numbers.append("Fizz")
    elif number%5 == 0:
        list_of_numbers.append("Buzz")
    else:
        list_of_numbers.append(number)

print(list_of_numbers)