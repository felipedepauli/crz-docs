const uniqueGreeting = Symbol('Dae rapeize! =D')    // fjdsfjdslkajfdslkjfsdalkj
const otherUniqueGre = Symbol('Dae rapeize! =D')    // jfelkw2431lkj321ljewjqalk

console.log('Os dois símbolos são iguais?', uniqueGreeting === otherUniqueGre)

// Eu criei o objeto abaixo com uma propriedade. Os symbols não são considerados propriedades.
let object = {
    [Symbol('name')]: 'Felipão',
    [Symbol('age')]: 38,
    city: 'Curita'
}

console.log('Array com as propriedades\t: ',Object.keys(object))
console.log('Número de propriedades\t\t: ',Object.keys(object).length)

const symbols = Object.getOwnPropertySymbols(object)

console.log(symbols)

// Symbols são utilizados principalmente para não se correr o risco de se ter duas propriedades com a mesma chave. Para acessar uma propriedade criada por symbols, é necessário utilizar a seguinte sintaxe:
const [name, age] = symbols.map(sym => object[sym])
console.log(name)
console.log(age)