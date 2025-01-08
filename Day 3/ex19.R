library(ggplot2)

ventes = data.frame(
  Mois = c("Janvier", "Février", "Mars", "Avril"),
  ChiffreAffaires = c(1000, 1200, 1500, 1700)
)

ventes

ggplot(
  ventes,
  aes(x = Mois, y = ChiffreAffaires)
) + geom_col(aes(fill = Mois)) + theme_minimal() + labs(title = "Totaux des ventes par mois",x = "Produits", y = "Chiffres d'Affaires (euros)")
