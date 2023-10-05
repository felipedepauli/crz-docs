const minhaString = 'Que texto grande, meu irmão!'

console.log('Começa com Que: ' + minhaString.startsWith('Que'))
console.log('Começa com Uei: ' + minhaString.startsWith('Uei'))

console.log('A partir do 3 char, tem texto: ' + minhaString.startsWith('texto', 3))
console.log('A partir do 4 char, tem texto: ' + minhaString.startsWith('texto', 4))

console.log('Termina com irmão: ' + minhaString.endsWith('irmão'))
console.log('Termina com irmão antes do ponto final: ' + minhaString.endsWith('irmão', minhaString.length -1))

console.log('Tem grande no meio: ', minhaString.includes('grande'))

