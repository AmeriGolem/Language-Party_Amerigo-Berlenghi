library(dplyr)
employes = data.frame(
  Nom = c("Alice", "Bob", "Clara", "David"),
  Departement = c("RH", "IT", "IT", "Finance"),
  Salaire = c(3000, 4500, 5000, 4000)
)

employes_IT = filter(employes, Departement == "IT")
print(employes_IT)

mean_salary = group_by(employes, mean)
mean_salary