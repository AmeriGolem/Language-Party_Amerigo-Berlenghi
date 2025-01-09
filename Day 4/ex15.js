panier = [
    {nom:"Brocoli", prix:7.59, quantite:2},
    {nom:"Poulet", prix:5.99, quantite:5},
    {nom:"Tiramisu", prix:13.19, quantite:1}
]

total = 0
for (let i=0; i<panier.length; i++) {
    total += panier[i].prix * panier[i].quantite
}
console.log(`Le total à payer est ${total}€.`)

panier.push({nom:"Fraise Tagada", prix:3.69, quantite:3})

// Let's remove the tiramisu
remove_word = "Tiramisu"

// answer from https://stackoverflow.com/questions/5767325/how-can-i-remove-a-specific-item-from-an-array-in-javascript
panier = panier.filter(item => item.nom !== remove_word)

console.log(panier)