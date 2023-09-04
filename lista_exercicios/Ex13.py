# Classe Funcionário: Implemente a classe Funcionário. Um empregado tem um nome (um string)
# e um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos
# para devolver nome e salário. Escreva um pequeno programa que teste sua classe.

class Funcionario():

    def __init__(self, salario):
        
        self.__funcionarioDados = {
            "nome": "",
            "salario": float(salario)
        }

    def getFuncionarioNome(self):
        return self.__funcionarioDados["nome"]

    def getFuncionarioSalario(self, salario):
        return self.__funcionarioDados["salario"], float(salario)

    def nomeFuncionario(self):
        self.__funcionarioDados["nome"] = str(input("Digite o nome do funcionário: "))
        return self.__funcionarioDados["nome"]

    def salarioFuncionario(self, salario):
        self.__funcionarioDados["salario"] = float(input("Digite o salário do funcionário: "))
        return self.__funcionarioDados["salario"], float(salario)

    def statusFuncionario(self, salario):
        print(f"O nome do funcionário é: {self.__funcionarioDados['nome']}")
        print(f"O salário do funcionário é: {self.__funcionarioDados['salario']}")
        return self.__funcionarioDados["nome"], self.__funcionarioDados["salario"]


    def menu(self):
        while True:
            print("1 - Nome\n2 - Salário\n3 - Dados Funcionario\n4 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    print(f"O nome do funcionário é: {self.nomeFuncionario()}")
                elif opcao == 2:
                    print(f"O salário do funcionário é: {self.salarioFuncionario(self.__funcionarioDados['salario'])}")
                elif opcao == 3:
                    self.statusFuncionario(0)
                elif opcao == 4:
                    print("Saindo...")
                    exit()
                else:
                    print("Digite um valor válido!")
            except ValueError:
                print("Caracter inválido!")


funcionario = Funcionario(0)
funcionario.menu()