function Pessoa() {
    if (!Pessoa.instance)   Pessoa.instance = this;
    return Pessoa.instance    
}