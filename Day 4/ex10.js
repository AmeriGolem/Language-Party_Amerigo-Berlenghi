numbers = []


for (let i = 0; i<50; i++) {
    rand = Math.round(1 + 99*Math.random())
    numbers.push(rand)
}

//answer from https://stackoverflow.com/questions/10359907/how-to-compute-the-sum-and-average-of-elements-in-an-array
// it is much shorter than the for loop, I will use it from now on

const sum = numbers.reduce((a, b) => a + b, 0);
const avg = (sum / numbers.length) || 0;

console.log(`The sum is: ${sum}. The average is: ${avg}.`);
// learned to use ... from https://stackoverflow.com/questions/1669190/find-the-min-max-element-of-an-array-in-javascript
console.log(`The max is: ${Math.max(...numbers)}. The min is: ${Math.min(...numbers)}.`)

even_numbers = 0
for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 == 0) {
        even_numbers += 1
    }
}

console.log(`There are ${even_numbers} even numbers in the array.`)