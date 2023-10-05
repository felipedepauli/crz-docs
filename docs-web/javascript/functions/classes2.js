const Character = require('./classes')

class Lemons extends Character {
    constructor(name, genre, species, creator, order){
        super(name, genre, species)
        this.creator = creator
        this.order = order
    }
    myCreator(){
        console.log(`Vou falar em english, now! My creator was ${this.creator}. I was the ${this.order} created.`)
    }
}

const Conde1 = new Lemons('Lemon Grab 1', 'male', 'limão', 'Jujuba', 'first')
const Conde3 = new Lemons('Lemon Grab 3', 'male', 'limão', 'Lemom Grab 1', 'third')


console.log('------')
Conde1.hello()
Conde1.myCreator()
console.log('------')
Conde3.hello()
Conde3.myCreator()