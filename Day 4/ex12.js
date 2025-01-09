endroit = {
    rue : "Passy",
    ville : "Paris",
    codePostal : "75016"
}
personne = {
    nom : "Alice",
    age : 30,
    adresse : endroit,
    hobbies : ["Lecture", "Natation", "Voyages"]
}

console.log(personne)

personne.hobbies.push("Manger")
personne.age = 20
delete personne.adresse.codePostal

console.log(personne)