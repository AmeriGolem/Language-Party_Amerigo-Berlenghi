class Animal:
    def __init__(self, nom:str, espece:str):
        self.nom = nom
        self.espece = espece
    
    def parler(self):
        return "Je suis un animal."
        
class Chien(Animal):
    def parler(self):
        return "Wouf"

class Chat (Animal):
    def parler(self):
        return "Miaou"
    
class Zoo:
    def __init__(self):
        self.animals = []
    
    def ajouter_animal(self, animal:Animal):
        self.animals.append(animal)
    
    def faire_parler_tout_le_monde(self):
        for animal in self.animals:
            print(animal.parler())

my_zoo = Zoo()
dog1 = Chien("Albert","Berger Mallinois")
dog2 = Chien("Céline", "Husky")
cat1 = Chat("Frank", "Sphynx")
cat2 = Chat("Duchesse", "Lynx")

for animal in [dog1, dog2, cat1, cat2]:
    my_zoo.ajouter_animal(animal)

my_zoo.faire_parler_tout_le_monde()