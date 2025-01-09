function calculer (first, second, operation) {
    if (operation == "+") {
        return first + second
    } else if (operation == "-") {
        return first - second
    } else if (operation == "*") {
        return first * second
    } else if (operation == "/") {
        return first / second
    }
}

console.log(calculer(5, 7, "*"))