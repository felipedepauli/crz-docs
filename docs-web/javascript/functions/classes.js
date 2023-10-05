const female = 'female'
const male   = 'male'

class Character {
    constructor(name, genre, species) {
        this.name = name
        this.genre = genre
        this.pronaum = genre === female ? 'uma' : 'um'
        this.species = species
    }
    hello () {
        console.log(`Olá! Meu nome é ${this.name}. Sou ${this.pronaum} ${this.species}.`)
    }
    static metodoExclusivoDaClasse(){
        console.log('Só funciono se for executado pela classe, não pelo objeto.')
    }
}

module.exports = Character

