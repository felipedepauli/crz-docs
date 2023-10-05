const myMap = new Map()
const apple = 'apple'
const orange = 'orange'
const satanas = 'satanas'

myMap.set('apple', 'fruit')
myMap.get(apple)


console.log(`My apple is a delicious ${myMap.get(apple)}!!!!`)

myMap.set('orange', 'fruit')
myMap.set('satanas', "very crazy guy")

console.log(`My orange is a delicious ${myMap.get(orange)}!!!!`)
console.log(`${satanas.charAt(0).toUpperCase() + satanas.slice(1)} is a ${myMap.get(satanas)}!!!`)