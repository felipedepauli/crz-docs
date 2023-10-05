const user = {
    name        : "Felipe",
    lastname    : "de Pauli"
}

const fullName = (user) => {
    return {
        ...user,
        fullname: `${user.name} ${user.lastname}`
    }
}

const felipe = fullName(user)
console.log(felipe.fullname)