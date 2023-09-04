# Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe
# contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor
# que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem
# parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
# poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o
# método adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento():

    def __init__(self):
        self.__saldo = 1000
        self.__taxaJuros = 10 / 100

    def getSaldo(self):
        return self.__saldo

    def getTaxaJuros(self):
        return self.__taxaJuros



    def adicioneJuros(self):
        self.__saldo += (self.__saldo * self.__taxaJuros)
        return self.__saldo

    def repetirJuros(self):
        for i in range(4):
            self.adicioneJuros()
            print(f"Seu saldo atual é de: {self.getSaldo()}")

    def menu(self):
        while True:
            print("1 - Ver saldo\n2 - Adicionar juros\n3 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    print(f"Seu saldo é de: {self.getSaldo()}")
                elif opcao == 2:
                    print(f"Seu saldo atual é de: {self.repetirJuros()}")
                elif opcao == 3:
                    break
                else:
                    print("Digite um valor válido!")
            except ValueError:
                print("Caracter inválido!")

conta = ContaInvestimento()
conta.menu()