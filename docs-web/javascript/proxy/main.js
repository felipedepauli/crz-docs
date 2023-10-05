const meuObjeto = {
    name: "LemonGrab",
    species: "lemon"
}

const meuProxy = new Proxy(meuObjeto, {
    get(target, name) {
        console.log('Alguém tá perguntando meu nome... =)')
        return `Meu nome é ${target[name]}.`
    },
    set(target, name, value) {
        console.log(`Alguém tá querendo alterar o parâmetro name. Vamos alterar...`)
        const nomeAntigo = target[name]
        target[name] = value
        return `Alterei de ${nomeAntigo} para ${value}`
    }
})

console.log(meuProxy.name)
