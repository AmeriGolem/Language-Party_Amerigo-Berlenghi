etudiant = data.frame(
    Nom = c("Alice", "Bob", "Clara", "David", "Emma", "Fred", "Gina"),
    Age = c(22, 25, 20, 23, 24, 26, 21),
    Note = c(15, 18, 14, 16, 17, 19, 20)
    )

print(subset(etudiant, select=c("Nom", "Note")))
print(subset(etudiant, Note >= 15 ))
