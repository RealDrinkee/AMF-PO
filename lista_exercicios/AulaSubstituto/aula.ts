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

