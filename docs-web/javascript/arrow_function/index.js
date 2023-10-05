const Paislandia = [
    {
        name: 'Gandolf',
        gender: 'male'
    },
    {
        name: 'Insane Mad Girl',
        gender: 'female'
    },
    {
        name: 'Cock',
        gender: 'male'
    },
    {
        name: 'Nataline',
        gender: 'female'
    }
]

const newPaislandia = Paislandia.map((valor, key)=>`${valor.gender=='female'?"Minha amiga":"Meu amigo"} ${valor.name} está na posição ${key}.`)

console.log(newPaislandia)

const femalePaislandia = Paislandia
                            .filter(({gender}) => gender == 'female')
                            .map(person => `A ${person.name} é uma mulher.`)
console.log('As mulheres são:')
console.log(femalePaislandia)