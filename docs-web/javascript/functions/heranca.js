// Herança prototipal

const female = 'female'
const male = 'male'

function meu_template(template, ...args) {
    return template.reduce((accumulator, insignificante, i) => {
        return `${accumulator}<div class="classe_insana">${template}</div>`
    })
}

function Characters(name, genre, species) {
//  Constructor
    this.name       = name
    this.genre      = genre
    this.species    = species
}
Characters.prototype.apresentacao = function() {
    console.log(meu_template`Olá! Meu nome é ${this.name}. Sou ${this.genre === female?"uma":"um"} ${this.species}.`)
}


const Jujuba    = new Characters('Bonnibel Bonnie Jujuba'   , female, "Humanoide de Chiclete")
const Marceline = new Characters('Marceline Abadeer'        , female, "Vampira" ) 

console.log(Jujuba)
console.log(Jujuba.species)
Marceline.apresentacao()

const message = document.querySelector('#message')
message.innerHTML = Marceline.apresentacao()