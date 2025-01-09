variable = "10, 20, 30, 40"
// Réponse de https://forums.waytolearnx.com/t/convertir-une-chaine-de-caracteres-en-tableau-en-javascript/382
table = JSON.parse("[" + variable + "]")

console.log(`Nombre de charactère: ${table.length}`)

somme = 0
for (let i = 0; i < table.length; i++) {
    somme += table[i]
}
console.log(`Somme des nombres: ${somme}`)

console.log(`Moyenne des nombres: ${somme/table.length}`)

nombre_au_dessus = 0
for (let i = 0; i < table.length; i++) {
    if (table[i] > (somme/table.length)) {
        nombre_au_dessus += 1
    }
}
console.log(`Nombre au dessus de moyenne: ${nombre_au_dessus}`)