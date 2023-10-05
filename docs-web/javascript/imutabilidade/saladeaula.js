const alunos = [
    {
        name    : "John Mackenbrow",
        grade   : 9
    },
    {
        name    : "Juscelino Kubicheck",
        grade   : 3
    },
    {
        name    : "Jair Bolsonaro",
        grade   : 0
    },
    {
        name    : "Heleninha Furacão",
        grade   : 10
    }
]

const verificaAprovados = (classe) => {
    return classe.filter((aluno) => {
        return aluno.grade >= 7
    })
}

const aprovados = verificaAprovados(alunos)
console.log(aprovados)