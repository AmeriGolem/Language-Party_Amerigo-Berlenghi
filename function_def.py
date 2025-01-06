def get_number(type:str="float")-> int:
    while True:
        print("Veuillez choisir un nombre")
        number_str = input()
        try:
            if type == "float":
                number = float(number_str)
            elif type == "int":
                number = int(number_str)
            break
        except ValueError:
            print(f"Votre choix n'est pas valide.")
    return number

# Stack Overflow answer
# https://stackoverflow.com/questions/22950768/random-int-without-importing-random
def rand_generator(seed, N=1, a=0, b=10, integer = True):
    '''For a given seed, this function returns N pseudo-random between a and b'''
    rands =[]
    if integer:
        for i in range(N):
            num = int(a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13)
            rands.append(num)
        return rands
    else:
        for i in range(N):
            num = a+(b-a)*(abs(hash(str(hash(str(seed)+str(i+1)))))%10**13)/10**13
            rands.append(num)
        return rands