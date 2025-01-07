class Livre:
    def __init__(self,titre:str,auteur:str,disponible:bool=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible
        
    def emprunter(self):
        if self.disponible:
            self.disponible = False
        else:
            print("Vous ne pouvez pas emprunter, le livre n'est pas disponible.")
    
    def rendre(self):
        self.disponible = True

class Utilisateur:
    def __init__(self, nom:str, livres_empruntes:list=[]):
        self.nom = nom
        self.livres_empruntes = livres_empruntes
    
    def emprunter_livre(self, livre:Livre):
        self.livres_empruntes.append(livre)
    
    def rendre_livre(self, livre:Livre):
        self.livres_empruntes.remove(livre)
        

class Bibliotheque:
    def __init__(self, book_list:list=[]):
        self.book_list = book_list
        self.book_name_list = []
        for book in self.book_list:
            self.book_name_list.append(book.titre)

    def ajouter_livre(self, livre:Livre):
        self.book_list.append(livre)
        self.book_name_list.append(livre.titre)

    def afficher_livres(self):
        for book in self.book_list:
            print(f"{book.titre} - disponible: {book.disponible}")

    def gerer_emprunt(self,livre:Livre, utilisiteur:Utilisateur, action:str):
        if action == "emprunt":
            if livre.disponible:
                utilisiteur.emprunter_livre(livre)
                livre.emprunter()
            else:
                print("Le livre n'est pas disponible.")
        elif action == "rendre":
            utilisiteur.rendre_livre(livre)
            livre.rendre()
        else:
            print("l'Action n'est pas compris.")
            
Alice = Livre("Alice au Pays des Merveille","Lewis Caroll")
Journey = Livre("Journey to the West","Wu Cheng'en")

Alpha = Utilisateur("Alpha")
Beta = Utilisateur("Beta")

ma_bibli = Bibliotheque([Alice, Journey])
ma_bibli.afficher_livres()

ma_bibli.gerer_emprunt(Alice,Alpha,"emprunt")
ma_bibli.gerer_emprunt(Alice,Beta,"emprunt")
ma_bibli.gerer_emprunt(Alice,Alpha,"rendre")
ma_bibli.gerer_emprunt(Alice,Beta,"emprunt")
ma_bibli.gerer_emprunt(Journey,Beta,"emprunt")
print("Les livres de Beta sont:", Beta.livres_empruntes)