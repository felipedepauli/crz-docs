let accumulator = 0;
let valorDeRetorno;

const minhaPromessa = () => new Promise((resolve) => {
  setTimeout(() => {
    accumulator += 1;
    resolve(accumulator);
  }, 1000);
});

// O await sempre deve ficar na frente de uma promessa. A função fetch é uma
// promessa. Qualquer função que tenha then e catch é uma promessa.

async function funcaoAssincrona() {
  try {
    valorDeRetorno = await minhaPromessa();
    console.log(valorDeRetorno);
    valorDeRetorno = await minhaPromessa();
    console.log(valorDeRetorno);
    valorDeRetorno = await minhaPromessa();
    console.log(valorDeRetorno);
    valorDeRetorno = await minhaPromessa();
    console.log(valorDeRetorno);
  } catch (err) {
    console.error('Eita Giovana...', err);
  }
}

funcaoAssincrona();
