class Produit:
    def __init__(self, nom:str, prix:float, quantite:int):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    
    def afficher_produit(self):
        print(f"Information sur {self.nom}:")
        print("le prix:", self.prix)
        print("la quantité:", self.quantite)
        

class Magasin:
    def __init__(self):
        self.product_list = []
    
    def ajouter_produit(self, produit:Produit):
        self.product_list.append(produit)
        print(produit.nom, "a été ajouté au magasin.")
        
    def rechercher_produit(self, product_name):
        match : Produit
        match_index : int
        for i in range(len(self.product_list)):
            if self.product_list[i].nom == product_name:
                match = self.product_list[i]
                match_index = i
                break
        return match, match_index
    
    def afficher_inventaire(self):
        print("Inventaire:")
        print(self.product_list)
        
    def vendre_produit(self, product_name):
        product, product_index = self.rechercher_produit(product_name)
        if self.product_list[product_index].quantite > 0:
            self.product_list[product_index].quantite -= 1 
            print(f'Le produit "{product.nom}" a été vendu.')
        else:
            print(f'Le produit "{product.nom}" est en rupture de stock.')

my_shop = Magasin()
produit1 = Produit("Ordinateur", 999.99, 5)
produit2 = Produit("Téléphone", 699.99, 10)
produit3 = Produit("Tablette", 299.99, 8)
produit4 = Produit("Imprimante", 89.99, 3)

for prod in  [produit1, produit2, produit3, produit4]:
    my_shop.ajouter_produit(prod)

my_shop.vendre_produit("Téléphone")
my_shop.vendre_produit("Tablette")
my_shop.vendre_produit("Téléphone")
my_shop.vendre_produit("Imprimante")
my_shop.vendre_produit("Téléphone")
my_shop.vendre_produit("Téléphone")
my_shop.vendre_produit("Ordinateur")