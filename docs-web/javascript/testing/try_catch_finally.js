// Let's try it.

const myFunction = (op) => {
    switch(op) {
        case 1:     throw "Amiguinho!"
        case 2:     throw "Eeee, caceta!"
        default:    break
    }
}


console.log("-------------------------")
// Caso 01: Erro identificado, jogado e recuperado
try {
    myFunction(1)       
}
catch(e) {
    console.log("Oi :", e)  // Tratado, mas sem o console.error
}
finally {
    console.log("Tudo bem??")
}


console.log("-------------------------")
// Caso 02: Identação de tries e catches
try {
    console.log("Vamos tentar")
    myFunction(2)
}
catch(e) {
    try {
        throw e
    }
    catch (e) {
        console.error("Agora tá limpo", e)  // Tratado e com console.error.
    }
}
finally {
    console.log("Satanás!")
}


console.log("-------------------------")
// Caso 03: Aqui o erro não foi tratado.
try {
    console.log("Vamos tentar")
    myFunction(2)
}
catch(e) {
    throw e // Aqui o erro foi jogado no ar sem catch
}
finally {
    console.log("Satanás!")
}

