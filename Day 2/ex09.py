class Article:
    def __init__(self, nom:str, prix:float, quantite:int):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
    
    def retirer_stock(self):
        if self.quantite > 0:
            self.quantite -= 1
        else:
            print("Il n'y as plus de stock.")

class Commande:
    def __init__(self, client:str, articles_commandes:list=[]):
        self.client =client
        self.articles_commandes = articles_commandes
    
    def calculer_total_et_commander(self):
        total = 0
        missing_articles = {}
        for article in self.articles_commandes:
            if article.quantite > 0:
                article.retirer_stock()
                total += article.prix
            else:
                if article.nom not in missing_articles:
                    missing_articles[article.nom] = 1
                else:
                    missing_articles[article.nom] += 1
        print(f"La commande a été faite.\nLe total de la commande s'élève à: {total}€")
        if len(missing_articles) > 0:
            print("Certains articles n'ont pas pu être acheter:")
            for article in missing_articles:
                print(f"- {article}: {missing_articles[article]}")

article1 = Article("Stylo plume", 12.99, 50)
article2 = Article("Carnet de notes", 8.49, 30)
article3 = Article("Clavier mécanique", 89.99, 15)
article4 = Article("Casque audio", 59.99, 20)
article5 = Article("Lampe de bureau", 25.00, 10)

commande1 = Commande("Alice Dupont", [article1, article2, article3])
commande2 = Commande("Jean Martin", [article1, article1, article3])

commande1.calculer_total_et_commander()
print()
commande2.calculer_total_et_commander()