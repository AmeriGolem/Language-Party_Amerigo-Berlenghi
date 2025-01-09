votes = ["Pomme", "Banane", "Orange", "Pomme", "Raisin", "Banane", "Banane"]
counts = {}

// count of occurence online https://stackoverflow.com/questions/5667888/counting-the-occurrences-frequency-of-array-elements
for (const num of votes) {
    counts[num] = counts[num] ? counts[num] + 1 : 1;
  }
  
  console.log(counts)

  // answer from https://stackoverflow.com/questions/27376295/getting-key-with-the-highest-value-from-object?noredirect=1&lq=1
  const getMax = object => {
    return Object.keys(object).filter(x => {
         return object[x] == Math.max.apply(null, 
         Object.values(object));
   });
};

console.log(`The element that has been voted the most is ${getMax(counts)}.`)