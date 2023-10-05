const myNumber = 12.04032

// Número para string
const myNumberAsAString = myNumber.toString()
console.log(typeof myNumberAsAString, myNumberAsAString)

// Duas casas decimais
const fixedTwoDecimals = myNumber.toFixed(2);
console.log(fixedTwoDecimals)

// Transforma uma string em float
const meuFloatinho = parseFloat(myNumberAsAString)
console.log(typeof meuFloatinho, meuFloatinho)

// Transforma uma string em int
const meuIntinho = parseInt(myNumberAsAString)
console.log(typeof meuIntinho, meuIntinho)