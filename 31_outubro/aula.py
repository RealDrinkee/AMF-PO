class Pessoa:

    def __init__(self, nome):
        self.nome = nome

class Professor(Pessoa):

    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

class Funcionario(Pessoa):

    def __init__(self, nome, cargo):
        super().__init__(nome)
        self.cargo = cargo

class Diretor(Professor, Funcionario):

    def __init__(self, nome, cargo, disciplina):
        self.nome = nome
        self.cargo = cargo
        self.disciplina = disciplina

if __name__ == "__main__":
    diretor = Diretor("JOAO", "Calculista", "Matematico")
    print(diretor.nome)
    print(diretor.cargo)
    print(diretor.disciplina)
