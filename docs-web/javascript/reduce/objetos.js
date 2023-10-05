// O reduce vai sempre reduzir um array a apenas um valor.
animais = [
    {
      nome: 'Fumaça',
      idade: 3,
      tipo: 'cao'
    },
    {
      nome: 'Tobby',
      idade: 6,
      tipo: 'cao'
    },
    {
      nome: 'Laminha',
      idade: 1,
      tipo: 'gato'
    },
    {
      nome: 'Nutella',
      idade: 3,
      tipo: 'cao'
    },
];

// É possível fazer isso de duas formas.
// A primeira é por concatenação do filter, map e reduce.
dogAgeSum = animais
                .filter((animal) => animal.tipo == 'cao')              
console.log(dogAgeSum) 
dogAgeSum = animais
                .filter((animal) => animal.tipo == 'cao')
                .map((cao) => cao.idade * 7)             
console.log(dogAgeSum)
dogAgeSum = animais
                .filter((animal) => animal.tipo == 'cao')
                .map((cao) => cao.idade * 7)
                .reduce((idadeTotal, cao) => idadeTotal += cao, 0)                
console.log(dogAgeSum)

//  A segunda é usando o reduce direto (mais utilizado****).
dogAgeSum = animais.reduce((idadeTotal, animal) => {
    if (animal.tipo == 'cao') return idadeTotal += ((animal.idade) * 7)
    else                      return idadeTotal
}, 0)
console.log('-----------')
console.log(dogAgeSum)