class Menu:
    def __init__(self, joueur, inventaire, liste_compétence):
        self.joueur = joueur
        self.inventaire = inventaire
        self.liste_compétence = liste_compétence

class Personnage:
    def __init__(self, nom:str, pv:int, force:int, pm:int, pc:int, vitesse:int, defense:int):
        self.nom = nom
        self.pv = pv
        self.pv_max = 25
        self.force = force
        self.force_max = 15
        self.pm = pm
        self.pm_max = 3
        self.pc = pc
        self.pc_max = 6
        self.vitesse = vitesse
        self.vitesse_max = 15
        self.defense = defense
        self.defense_max = 15
        self.niveau = 0
        self.NIVEAU_MAX = 10
        self.xp = 0
        self.BAR_XP = [5, 7, 11, 16, 25, 37, 56, 85, 128, 192]
        