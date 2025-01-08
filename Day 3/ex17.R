notes = data.frame(
  Nom = c("Alice", "Bob", "Clara"),
  Note1 = c(15, 10, 12),
  Note2 = c(17, 14, 9)
)

notes$Moyenne = apply(notes[,c("Note1", "Note2")],1, mean)

notes
