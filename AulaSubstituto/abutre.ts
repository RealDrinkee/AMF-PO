interface Animal {
    dorme(): void;
    come(): void;
    nome: {
        primeiroNome: string;
        ultimoNome: string;
    }
}

const vaca: Animal = {
    dorme() {
        console.log('Dorme')
    },
    come() {
        console.log('Come')
    }
}

nome: 'Jurema'