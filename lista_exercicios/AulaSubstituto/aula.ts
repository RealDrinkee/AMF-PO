interface AnimalBackend {
    nome: string;
}

const animal = {
    nome: 'Cachorro',
}
function getNomeSobrenome(animal: AnimalBackend) {
    const split = animal.nome.split(' ');
    return {
        nome: split[0],
        sobrenome: split.slice(1).join(' '),
    }
}

class Vaca extends Animal {
    constructor(nome: string) {
        super(nome);
    }
}

function recebeAnimal(animal: Animal) {
    if(animal instanceof Vaca) {
        print("Muuuuu")
}

class Animal implements AnimalBackend {
    constructor(public nome: string) {
        this.nome = nome;
    }
}

const animal2 = new Animal('Cachorro');

console.log(getNomeSobrenome(animal2));