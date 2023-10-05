const vetorinho = new Array()

var accumulator = 0
var retornoDeDados

const buscaDadosNoBanco = () => new Promise((resolve, reject) => {
    setTimeout(()=> {
        resolve(accumulator++)
    }, 2000)
})
// Perceba que o argumento passado para o next vira retorno do yield.
function* buscarDados() {
    retornoDeDados = yield buscaDadosNoBanco().then((dadosRecebidos)=>dados.next(dadosRecebidos))
    console.log(retornoDeDados)

    retornoDeDados = yield buscaDadosNoBanco().then((dadosRecebidos)=>dados.next(dadosRecebidos))
    console.log(retornoDeDados)

    retornoDeDados = yield buscaDadosNoBanco().then((dadosRecebidos)=>dados.next(dadosRecebidos))
    console.log(retornoDeDados)

    retornoDeDados = yield buscaDadosNoBanco().then((dadosRecebidos)=>dados.next(dadosRecebidos))
    console.log(retornoDeDados)
}

const dados = buscarDados()
dados.next()