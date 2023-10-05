// new Error (message, fileName, lineNumber);

const MeuErro = new Error ("Eitaaaa Giovanaaaaa");

console.log(MeuErro.name);
console.log(MeuErro.fileName)
console.log(MeuErro.lineNumber)
console.log(MeuErro.message)
console.log(MeuErro.stack)
console.log(MeuErro.)

try {
    throw MeuErro
}
catch(e) {
    console.error(e)
}