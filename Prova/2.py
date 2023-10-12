from abc import ABC, abstractmethod

class Disciplina(ABC):
    def __init__(self, nome, carga_horaria):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.primeira_nota = 0
        self.segunda_nota = 0

    @abstractmethod
    def avaliacao(self):
        pass

class DisciplinaTrimestral(Disciplina):
    def avaliacao(self):
        self.primeira_nota = float(input("Digite a primeira nota: "))
        self.segunda_nota = float(input("Digite a segunda nota: "))
        self.media = (self.primeira_nota * 0.4) + (self.segunda_nota * 0.6)
        print("A média é:", self.media)

class DisciplinaSemestral(Disciplina):
    def __init__(self, nome, carga_horaria):
        super().__init__(nome, carga_horaria)
        self.terceira_nota = 0

    def avaliacao(self):
        self.primeira_nota = float(input("Digite a primeira nota: "))
        self.segunda_nota = float(input("Digite a segunda nota: "))
        self.terceira_nota = float(input("Digite a terceira nota: "))
        self.media = (self.primeira_nota + self.segunda_nota + self.terceira_nota) / 3
        print("A média é:", self.media)

class DisciplinaAnual(Disciplina):
    def __init__(self, nome, carga_horaria):
        super().__init__(nome, carga_horaria)
        self.terceira_nota = 0
        self.quarta_nota = 0
        self.quinta_nota = 0

    def avaliacao(self):
        self.primeira_nota = float(input("Digite a primeira nota: "))
        self.segunda_nota = float(input("Digite a segunda nota: "))
        self.terceira_nota = float(input("Digite a terceira nota: "))
        self.quarta_nota = float(input("Digite a quarta nota: "))
        self.quinta_nota = float(input("Digite a quinta nota: "))
        self.media = (self.primeira_nota + self.segunda_nota + self.terceira_nota + self.quarta_nota + self.quinta_nota) / 5
        print("A média é:", self.media)

def main():
    opcao = input("Escolha o tipo de disciplina (T/Trimestral, S/Semestral, A/Anual): ")
    nome = input("Digite o nome da disciplina: ")
    carga_horaria = int(input("Digite a carga horária da disciplina: "))

    if opcao.lower() == 't':
        disciplina = DisciplinaTrimestral(nome, carga_horaria)
    elif opcao.lower() == 's':
        disciplina = DisciplinaSemestral(nome, carga_horaria)
    elif opcao.lower() == 'a':
        disciplina = DisciplinaAnual(nome, carga_horaria)
    else:
        print("Opção inválida.")
        return

    disciplina.avaliacao()

if __name__ == "__main__":
    main()
