# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
# seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero
# e os demais atributos são obrigatórios.

class ContaCorrente():
    def __init__(self):
        self.numeroConta = 0
        self.nomeCorrentista = ""
        self.saldo = 0

    def alterarNome(self):
        self.nomeCorrentista = str(input("Digite o nome do correntista: "))
        return self.nomeCorrentista

    def deposito(self):
        valor = float(input("Digite o valor do depósito: "))
        if valor < 0:
            print("Valor inválido")
        else:
            print(f"Depósito realizado com sucesso R${valor:.2f}")
            self.saldo += valor
        return self.saldo

    def sacar(self):
        valor = float(input("Digite o valor do saque: "))
        if valor > 0:
            if valor > self.saldo:
                print("Saldo insuficiente")
            else:
                print(f"Saque realizado com sucesso R${valor:.2f}")
                self.saldo -= valor
            print("Valor inválido")
        else:
            print("Valor inválido")

    def menu(self):
        print("1 - Alterar nome\n2 - Depósito\n3 - Saque\n4 - Mostrar saldo\n5 - Sair")
        escolha = int(input("Escolha uma opção: "))
        return escolha

    def main(self):
        while True:
            escolha = self.menu()
            try:
                if escolha == 1:
                    self.alterarNome()
                elif escolha == 2:
                    self.deposito()
                elif escolha == 3:
                    self.sacar()
                elif escolha == 4:
                    print(f"Saldo: R${self.saldo:.2f}")
                elif escolha == 5:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Valor inválido")

contaCorrente = ContaCorrente()
contaCorrente.main()