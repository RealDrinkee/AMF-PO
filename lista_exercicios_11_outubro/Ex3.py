from abc import ABC, abstractmethod

class ErrorMenuDeEscolha(Exception):
    pass

class polimorfismo_clientes(ABC):

    @abstractmethod
    def dados_cliente(self):
        self.nome = input("Digite seu nome: ")
        self.cpf = input("Digite seu CPF: ")
        self.email = input("Digite seu email: ")

    @abstractmethod
    def escolha_pacote_de_viagem(self):
        pass

    @abstractmethod
    def escolha_hotel(self):
        pass

    @abstractmethod
    def escolha_voo(self):
        pass

class calcular_escolha_cliente(polimorfismo_clientes):

    def __init__(self, menu):
        super().__init__()
        self.menu = menu

    def receber_dados_cliente(self):
        super().dados_cliente()
        return self.nome, self.cpf, self.email

    def calcular_escolha_cliente(self):
        self.hotel = 0
        self.voo = 0
        self.numeros_passageiros = int(input("Digite o número de passageiros: "))

        print(f"Olá {self.nome}!")
        print("Escolha o pacote de viagem: ")
        print("1 - Voo Classe A\n2 - Voo Classe B\n3 - Voo Classe C")

        while True:
            escolha_cliente = input("Escolha o pacote de viagem: ")
            try:
                escolha_cliente = int(escolha_cliente)
                if escolha_cliente == 1:
                    self.hotel = 1500
                    self.voo = 2000
                elif escolha_cliente == 2:
                    self.hotel = 1000
                    self.voo = 1500
                elif escolha_cliente == 3:
                    self.hotel = 500
                    self.voo = 1000
                else:
                    raise ErrorMenuDeEscolha
                break
            except ValueError:
                print("Opção inválida")
            except ErrorMenuDeEscolha:
                print("Opção inválida")

        self.valor_total = (self.hotel + self.voo) * self.numeros_passageiros
        print(f"O valor total da viagem é: {self.valor_total}")
        self.pagamento()

    def pagamento(self):
        print("Escolha a forma de pagamento: ")
        print("1 - Cartão de Crédito\n2 - Cartão de Débito\n3 - Boleto")

        while True:
            try:
                self.forma_pagamento = int(input("Escolha a forma de pagamento: "))
                if self.forma_pagamento in [1, 2]:
                    self.valor_pagamento = float(input("Digite o valor do pagamento: "))
                    if self.valor_pagamento >= self.valor_total:
                        print("Pagamento realizado com sucesso!")
                        self.menu.escolher_menu()
                        break
                    else:
                        print("Saldo insuficiente")
                elif self.forma_pagamento == 3:
                    print("Pagamento realizado com sucesso!")
                    self.menu.escolher_menu()
                    break
                else:
                    raise ErrorMenuDeEscolha
            except ValueError:
                print("Opção inválida")
            except ErrorMenuDeEscolha:
                print("Opção inválida")


class cliente_viagem(calcular_escolha_cliente):

    def dados_cliente(self):
        super().dados_cliente()

    def escolha_pacote_de_viagem(self):
        pass

    def escolha_hotel(self):
        pass

    def escolha_voo(self):
        pass



class menu_escolha_cliente:

    def escolher_menu(self):
        print("Escolha uma opção: ")
        print("1 - Escolher\n2 - Sair")

        while True:
            try:
                self.escolha_menu = int(input("Escolha uma opção: "))
                if self.escolha_menu == 1:
                    cliente = cliente_viagem(self)
                    cliente.receber_dados_cliente()
                    cliente.calcular_escolha_cliente()
                elif self.escolha_menu == 2:
                    print("Obrigado por utilizar nosso sistema!")
                    exit()
                else:
                    raise ErrorMenuDeEscolha
            except ValueError:
                print("Opção inválida")
            except ErrorMenuDeEscolha:
                print("Opção inválida")

if __name__ == "__main__":
    menu = menu_escolha_cliente()
    menu.escolher_menu()
