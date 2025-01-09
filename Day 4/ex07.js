//numbers = [1, 4, 7, 2, 9, 3, 6, 8, 10, 5]
numbers = []

if (numbers.length > 0) {
    somme = 0
    for (let i = 0; i < numbers.length; i++) {
        somme += numbers[i]
    }
    console.log(`Moyenne des nombres: ${somme/numbers.length}`)
} else {
    console.log("Le tableau est vide")
}