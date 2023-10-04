import abc

class Funcionario(abc.ABC): # ABC = Abstract Base Class
    @abc.abstractmethod
    def calcular_salario(self):
        pass

class Gerente(Funcionario): # Herança concreta
    def calcular_salario(self):
        return 10000

class Diretor(Funcionario): # Herança concreta
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def calcular_salario(self):  # Implementar el método abstracto
        return self.salario

if __name__ == "__main__":
    gerente = Gerente()
    print(gerente.calcular_salario())

    diretor = Diretor("Joao", "123456789", 20000)
    print(diretor.calcular_salario())