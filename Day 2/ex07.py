from abc import ABC, abstractmethod
class Employe(ABC):
    def __init__(self, nom:str, salaire_base:int):
        self.nom = nom
        self.salaire_base = salaire_base
    
    @abstractmethod 
    def calculer_salaire (self):
        pass

class EmployeMensuel(Employe):
    def calculer_salaire(self):
        return self.salaire_base 

class EmployeHoraire(Employe):
    def calculer_salaire(self, hours_worked):
        return self.salaire_base * hours_worked

class Entreprise():
    def __init__(self, list_employees:list = []):
        self.list_employees = list_employees
    
    def show_salary_all (self, hours_worked):
        total = 0
        for employee in self.list_employees:
            if type(employee) == EmployeMensuel:
                total += employee.calculer_salaire()
            elif type(employee) == EmployeHoraire:
                total += employee.calculer_salaire(hours_worked)
        
        print("Le total à payer est", total, "euros.")

employee1 = EmployeMensuel("The One and Only", 2500)
employee2 = EmployeHoraire("Flexi-man", 20)
employee3 = EmployeMensuel("Mono-salary", 3000)
employee4 = EmployeHoraire("Francis", 15)

my_comp = Entreprise([employee1, employee2, employee3, employee4])

my_comp.show_salary_all(12)