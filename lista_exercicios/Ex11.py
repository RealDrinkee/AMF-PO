# Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
# 1. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
# quantidade de combustível no tanque.
# 2. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# 3. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
# reduzindo o nível de combustível no tanque de gasolina.
# 4. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# 5. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
# meuFusca = Carro(15); # 15 quilômetros por litro de combustível.
# meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível.
# meuFusca.andar(100); # anda 100 quilômetros.
# meuFusca.obterGasolina() # Imprime o combustível que resta no tanque.


class Carro():

    def __init__(self):
        self. __gasolinaPreco = 5.88
        self.__carro_escolhido = None
        self.__fusca1977 = {"tanque": 0, "consumo": 10}
        self.__BMW = {"tanque": 0, "consumo": 15}
        self.__tanque = 0

    def getInit(self):
        return self.__tanque, self.__gasolinaPreco, self.__carro_escolhido, self.__fusca1977, self.__BMW


    def selecionarCarro(self):
        print("1 - Fusca 1977\n2 - BMW\n3 - Sair")
        while True:
            opcao = int(input("Qual carro deseja? "))
            try:
                if opcao == 1:
                    self.__carro_escolhido = self.__fusca1977
                    self.menu()
                    return self.__carro_escolhido
                elif opcao == 2:
                    self.__carro_escolhido = self.__BMW
                    self.menu()
                    return self.__carro_escolhido
                elif opcao == 3:
                    self.menu()
                else:
                    print("Digite um valor válido!")
            except ValueError:
                print("Caracter inválido!")

            return self.__carro_escolhido

    def andarCarro(self):
        if self.__carro_escolhido is None:
            print("Selecione um carro!")
            self.selecionarCarro()
        elif self.__carro_escolhido["tanque"] <= 0:
            print("O tanque está vazio!")
        else:
            self.__tanque = int(input("Quantos quilômetros deseja andar? "))
            if self.__tanque > (self.__carro_escolhido["tanque"] * self.__carro_escolhido["consumo"]):
                print("Você não tem combustível suficiente para andar essa distância!")
            else:
                print(f"Você andou {self.__tanque} km")
                self.__carro_escolhido["tanque"] -= (self.__tanque / self.__carro_escolhido["consumo"])
            return self.__carro_escolhido["tanque"]
    def abasterCarro(self):
        if self.__carro_escolhido is None:
            print("Selecione um carro!")
            self.selecionarCarro()
        else:
            self.__tanque = int(input("Quantos litros deseja abastecer? "))
            self.__carro_escolhido["tanque"] += self.__tanque
            return self.__carro_escolhido["tanque"]

    def statusCarro(self):
        if self.__carro_escolhido is None:
            print("Selecione um carro!")
            self.selecionarCarro()
        else:
            print(f"O carro escolhido é: {self.__carro_escolhido}")
            print(f"O tanque está com: {self.__carro_escolhido['tanque']} litros")

    def menu(self):
        while True:
            print("1 - Selecionar carro\n2 - Abastecer carro\n3 - Andar com o carro\n4 - Status do carro\n5 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    self.selecionarCarro()
                elif opcao == 2:
                    self.abasterCarro()
                elif opcao == 3:
                    self.andarCarro()
                elif opcao == 4:
                    self.statusCarro()
                elif opcao == 5:
                    print("Saindo...")
                    exit()
                else:
                    print("Digite um valor válido!")
            except ValueError:
                print("Caracter inválido!")

carro = Carro()
carro.menu()

