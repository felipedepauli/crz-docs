function soma(a) {
    return function(b) {
        return a + b
    }
}

// Agora a gente cria a função já com o parâmetro desejado fixo.
const soma3 = soma(3)

console.log(soma3(3)) // Vai dar 6
console.log(soma3(5)) // Vai dar 8

