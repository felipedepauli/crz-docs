class User {
    constructor(){
        this.meu_amiguinho=" Satanás"
    }
    vamosLa(){
        function morri() {
            console.log(this.meu_amiguinho)
        }
        const wow = () => {
            console.log(this.meu_amiguinho)
        }
        // morri()
        wow()
    }
}

const Satanas = new User()
Satanas.vamosLa()
