ventes = data.frame(
  Produit = c("Pomme", "Orange", "Banane", "Raisin"),
  Quantite = c(50, 30, 20, 15),
  PrixUnitaire = c(1.2, 0.8, 0.5, 2.0)
)

ventes$Total = ventes$Quantite * ventes$Prix

cat("Les valeurs de la colonne Total sont:", ventes$Total)