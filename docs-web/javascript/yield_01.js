function getNames() {
    console.log('Willian')
    console.log('Jonas')
    console.log('Gabriel')
}

getNames()

function* genNames() {
    console.log('Chamando 1o nome.')
    yield 'Felipe'
    console.log('Chamando 2o nome.')
    yield 'Heleninha'
    console.log('Chamando 3o nome.')
    yield 'Heitorzim'
    console.log('Chamando 4o nome.')
    yield 'Hortência'
}

const names = genNames()

console.log(`Isto aqui é um ${names.next().value}.`)
console.log(`Isto aqui é um ${names.next().value}.`)
console.log(`Isto aqui é um ${names.next().value}.`)
console.log(`Isto aqui é um ${names.next().value}.`)