numbers = [1, 4, 7, 2, 9, 3, 6, 8, 10, 5]

let max_number = 0

for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > max_number) {
        max_number = numbers[i]
    }
}

console.log(max_number)