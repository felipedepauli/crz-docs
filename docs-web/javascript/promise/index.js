var defer  = new Promise((resolve, reject) => {
    setTimeout(() => {
        if (true) {
            console.log('Wowowow')
            resolve('Hey! It works.')
        } else {
            reject('Slk!')
        }
    }, 2000)
})

defer   
    .then( data => {
        console.log(data)
        return 10
    })
    .then( data => {
        console.log(data)
    })
    .catch( err => {
        console.log(err)
    })