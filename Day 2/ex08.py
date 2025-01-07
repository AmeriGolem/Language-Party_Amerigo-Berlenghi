class Reservation:
    def __init__(self, id, client, date, place):
        self.id = id
        self.client = client
        self.client.effectuer_reservation(self)
        self.date = date
        self.place = place
        self.status = "Non confirmée"
    
    def confirmer(self):
        self.status = "Confirmée"
        

class Client:
    def __init__(self, nom:str, email:str, reservations:list=[]):
        self.nom = nom
        self.email = email
        self.reservations = reservations
    
    def effectuer_reservation(self, reservation:Reservation):
        self.reservations.append(reservation)
        reservation.confirmer()


class SystemeDeReservation:
    def __init__(self, list_of_reservations:list=[]):
        self.list_of_reservations = list_of_reservations
    
    def ajouter_reservation(self, reservation:Reservation):
        self.list_of_reservations.append(reservation)
    
    def annuler_reservation(self, reservation: Reservation):
        reservation.status = "annulé"
    
    def afficher_reservations(self):
        print("Les réservations:")
        for res in self.list_of_reservations:
            print(res.id)


client1 = Client("Elara Lunemont", "elara.lunemont@example.com")
client2 = Client("Théo Clairval", "theo.clairval@example.com")
client3 = Client("Soline Mirabeau", "soline.mirabeau@example.com")

reservation_system = SystemeDeReservation()

reservation1 = Reservation(1, client1, "2025-01-15", "Paris")
reservation2 = Reservation(2, client2, "2025-02-20", "Lyon")
reservation3 = Reservation(3, client3, "2025-03-10", "Marseille")

for res in [reservation1, reservation2, reservation3]:
    reservation_system.ajouter_reservation(res)

reservation_system.annuler_reservation(reservation2)
reservation_system.afficher_reservations()
    