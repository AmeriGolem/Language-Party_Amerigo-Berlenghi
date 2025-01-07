class Plat:
    def __init__(self, nom, prix, temps_preparation):
        self.nom = nom
        self.prix = prix
        self.temps_preparation = temps_preparation
    
    def afficher_details(self):
        print(f"{self.nom}:")
        print("- prix:", self.prix)
        print("- temps de préparation", self.temps_preparation)
        
class Serveur:
    def __init__(self, nom, commandes_prises):
        pass