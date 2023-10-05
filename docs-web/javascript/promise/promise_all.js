// Este é o banco de dados (mongodb, por exemplo)
const items = ['a', 'b', 'c', 'd']

// Esta é uma função que precisará receber os valores do banco de dados.
;(async function() {
    // Ela gera uma promessa, que nada mais é do que uma função que, apesar de em tempo real
    // não retornar aquilo que precisar retornar, promete retornar assim que receber alguns
    // valores que precisa para realizar sua mágica.
    const promiseFunction = async (element) => {
        return new Promise((resolve, reject) => {
            return resolve(`${element} - promise`)
        })
    }

    const itemsMappedPromises = items.map(promiseFunction)
    const itemsMapped = await Promise.all(itemsMappedPromises)


    console.log(itemsMapped)
})()