import time

class Voiture:
    def __init__(self, marque:str, modele:str, annee:int, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
    
    def afficher_details(self):
        print("Détails de la voiture:")
        print("la marque:", self.marque)
        print("le modèle:", self.modele)
        print("l'année:", self.annee)
        print("le kilometrage:", self.kilometrage)
    
    def augmenter_kilometrage(self, increase_amount):
        self.kilometrage += increase_amount

    def calculer_age(self)->int:
        return 2025 - self.annee
    
    def est_vieille(self)->bool:
        return self.calculer_age() > 10

car1 = Voiture("renault", "zoe", 2016, 40.0)
car1.augmenter_kilometrage(250)
car1.afficher_details()
print(car1.est_vieille())

print()

car2 = Voiture("nissan", "juke", 2025, 25)
car2.augmenter_kilometrage(150.4)
car2.afficher_details()
print(car2.est_vieille())

print()

car3 = Voiture("Wolkswagen", "idk", 2010, 1754.6)
car3.augmenter_kilometrage(35)
car3.afficher_details()
print(car3.est_vieille())