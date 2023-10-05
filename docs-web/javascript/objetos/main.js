const entidade1 = {
    nome: 'Satanás',
    sobrenome: 'de Deus',
    idade: 100
}
const entidade2 = {
    nome: 'Saci',
    sobrenome: 'Pererê',
    idade: 200
}
console.log(Object.assign(entidade1, {nomeCompleto: `${entidade1.nome} ${entidade1.sobrenome}`}))
console.log(Object.assign({}, entidade2, {nomeCompleto: `${entidade2.nome} ${entidade2.sobrenome}`}))

console.log(entidade1)
console.log(entidade2)

// Object.freeze e Object.seal