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
    def __init__(self, nom, commandes_prises:list=[]):
        self.nom = nom
        self.commandes_prises = commandes_prises
    
    def prendre_commande(self, liste_de_plats:list=[]):
        self.commandes_prises.append(liste_de_plats)

class Client:
    def __init__(self, nom, commandes:list=[]):
        self.nom = nom
        self.commandes = commandes
    
    def add_order(self, order:Plat):
        self.commandes.append(order)
    
class Restaurant:
    def __init__(self, plats_disponible:list=[], serveurs_disponible:list=[], clients:list=[]):
        self.plats_disponible = plats_disponible
        self.serveurs_disponible = serveurs_disponible
        self.clients = clients
    
    def afficher_menu(self):
        print("MENU")
        for plat in self.plats_disponible:
            plat.afficher_details()
            print()
    
    def gerer_commandes(self):
        for client in self.clients:
            commande = client.commandes
            for serveur in self.serveurs_disponible:
                if len(serveur.commandes_prises) == 0:
                    serveur.prendre_commande(commande)
        print("Commandes attribuées")
        

plat1 = Plat("Spaghetti Carbonara", 12.50, 15)
plat2 = Plat("Pizza Margherita", 10.00, 20)
plat3 = Plat("Tiramisu", 6.50, 10)

serveur1 = Serveur("Lucas")
serveur2 = Serveur("Simon")
serveur3 = Serveur("Marguerite")

client1 = Client("Marie Dupont", [plat1, plat3])
client2 = Client("Annie McBeth", [plat3, plat1, plat2])

my_restaurant = Restaurant([plat1, plat2, plat3], [serveur1, serveur2, serveur3], [client1, client2])
my_restaurant.afficher_menu()
my_restaurant.gerer_commandes()