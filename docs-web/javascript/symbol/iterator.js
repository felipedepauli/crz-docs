Symbol.iterator
Symbol.split
Symbol.toStringTag

const my_set = [1, 2, 3, 4, 5, 6]
const it     = my_set[Symbol.iterator]()

while (true) {
    let {value, done} = it.next()
    if (done) break
    else console.log(value)
}