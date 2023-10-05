const satanas = [1, 2, 3, 5, 6, 7, 8, 9]

const decompor = (a, b, ...rest) => {
    console.log(`A variável a recebeu ${a}`)
    console.log(`A variável b recebeu ${b}`)
    console.log(`O vetorial rest recebeu ${rest}`)
    console.log(typeof(rest))
    
}

decompor(...satanas)