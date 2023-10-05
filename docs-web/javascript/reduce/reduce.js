const amigos = [
    {
        name: "Magda",
        age: 11
    },
    {
        name: "Jana",
        age: 11
    },
    {
        name: "Tião",
        age: 11
    },
    {
        name: "Magnólia",
        age: 11
    },
]


somaDasIdades = amigos.reduce((age, obj) => age += obj.age, 0)
console.log(somaDasIdades)