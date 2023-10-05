const female = 'female'
const male   = 'male'

const Character = require('./classes')

const Maga = new Character('Maga Caçadora', female, 'Humanoide')

Maga.hello()
console.log('Consigo acessar diretamente, também:', Maga.name)

Character.metodoExclusivoDaClasse()