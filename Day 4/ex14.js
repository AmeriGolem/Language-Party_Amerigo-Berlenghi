etudiants = [
    {nom : "Alice", "age": 19, note: 16},
    {nom : "Bob", "age": 18, note: 14},
    {nom : "Carl", "age": 20, note: 20},
    {nom : "Morgane", "age": 19, note: 18}
]

best_student = {note: 0}
for (let i=0; i<etudiants.length; i++) {
    if (etudiants[i].note > best_student.note) {
        best_student = etudiants[i]
    }
}
console.log(`Le meilleur étudiant est ${best_student.nom}.`)

above_students = []

for (let i=0; i < etudiants.length; i++) {
    if (etudiants[i].note >= 15) {
        above_students.push(etudiants[i].nom)
    }
}

console.log(`Les élèves qui ont une note plus grande que 15 sont ${above_students}.`)

sum = 0
for (let i=0; i < etudiants.length; i++) {
    sum += etudiants[i].note
}
mean = sum / etudiants.length

console.log(`La moyenne des étudiants est ${mean}.`)