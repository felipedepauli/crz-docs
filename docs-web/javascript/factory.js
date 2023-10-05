function Pessoa(customProperties){
    return {
        name: "John",
        lastName: "Mackenbrow",
        ...customProperties
    }
}

const inquilino = Pessoa({name: "Hannibal", age: 31})

console.log(inquilino)

const inquilino2 = Pessoa({age: 31})

console.log(inquilino2)