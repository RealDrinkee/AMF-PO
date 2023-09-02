# Classe Macaco: Desenvolva uma classe Macaco, que possua os atributos nome e bucho
# (estômago) e, pelo menos, os métodos comer(), verBucho() e digerir(). Faça um programa ou
# teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3
# alimentos diferentes e verificando o conteúdo do estômago a cada refeição. Experimente fazer
# com que um macaco coma o outro. É possível criar um macaco canibal?

class Macaco():

    def __init__(self):
        self.__macaco1 = {
            "nome": "",
            "bucho": []
        }

        self.__macaco2 = {
            "nome": "",
            "bucho": []
        }

    def setNome(self):
        self.__macaco1["nome"] = input("Qual o nome do primeiro macaco? ")
        self.__macaco2["nome"] = input("Qual o nome do segundo macaco? ")
        return self.__macaco1["nome"], self.__macaco2["nome"]

    def getMacacos(self):
        return self.__macaco1, self.__macaco2

    def comer(self):
        print("1 - Maça \n2 - Banana\n3 - Macaco\n4 - Sair")
        while True:
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    qualMacaco = int(input("Qual macaco deseja alimentar? 1 ou 2? "))
                    if qualMacaco == 1:
                        self.__macaco1["bucho"].append("Maça")
                        print(f"O macaco {self.__macaco1['nome']} comeu uma maça")
                        print(f"O macaco {self.__macaco1['nome']} está comendo: {self.__macaco1['bucho']}")
                    elif qualMacaco == 2:
                        self.__macaco2["bucho"].append("Maça")
                        print(f"O macaco {self.__macaco2['nome']} comeu uma maça")
                        print(f"O macaco {self.__macaco2['nome']} está comendo: {self.__macaco2['bucho']}")
                    else:
                        print("Digite um valor válido!")
                        self.comer()

                elif opcao == 2:
                    qualMacaco = int(input("Qual macaco deseja alimentar? 1 ou 2? "))
                    if qualMacaco == 1:
                        self.__macaco1["bucho"].append("Banana")
                        print(f"O macaco {self.__macaco1['nome']} comeu uma banana")
                        print(f"O macaco {self.__macaco1['nome']} está comendo: {self.__macaco1['bucho']}")
                    elif qualMacaco == 2:
                        self.__macaco2["bucho"].append("Banana")
                        print(f"O macaco {self.__macaco2['nome']} comeu uma banana")
                        print(f"O macaco {self.__macaco2['nome']} está comendo: {self.__macaco2['bucho']}")
                    else:
                        print("Digite um valor válido!")
                        self.comer()

                elif opcao == 3:
                    qualMacaco = int(input("Qual macaco deseja alimentar? 1 ou 2? "))
                    if qualMacaco == 1:
                        print("O macaco 1 comeu o macaco 2")
                        print("GAME OVER")
                        print("O macaco iniciou um apocalypse")
                        exit()
                    elif qualMacaco == 2:
                        print("O macaco 2 comeu o macaco 1")
                        print("GAME OVER")
                        print("O macaco iniciou um apocalypse")
                        exit()
                    else:
                        print("Digite um valor válido!")
                        self.comer()

                elif opcao == 4:
                    print("Retornando ao menu...")
                    self.menu()


                else:
                    print("Digite um valor válido!")

            except ValueError as error:
                print("Digite um valor válido!")
                print(error)

    def verBucho(self):
        while True:
            selecionarMacaco = int(input("Qual macaco deseja ver o bucho? 1 ou 2? "))
            try:
                if selecionarMacaco == 1:
                    print(f"O macaco {self.__macaco1['nome']} está comendo: {self.__macaco1['bucho']}")
                    self.menu()
                elif selecionarMacaco == 2:
                    print(f"O macaco {self.__macaco2['nome']} está comendo: {self.__macaco2['bucho']}")
                    self.menu()
                else:
                    print("Digite um valor válido!")
            except ValueError as error:
                print("Digite um valor válido!")
                print(error)

    def digerirComida(self):
        while True:
            selecionarMacaco = int(input("Qual macaco deseja digerir a comida? 1 ou 2?"))
            try:
                if selecionarMacaco == 1:
                    self.__macaco1["bucho"].clear()
                    print(f"O macaco {self.__macaco1['nome']} está comendo: {self.__macaco1['bucho']}")
                    self.menu()
                elif selecionarMacaco == 2:
                    self.__macaco2["bucho"].clear()
                    print(f"O macaco {self.__macaco2['nome']} está comendo: {self.__macaco2['bucho']}")
                    self.menu()
                else:
                    print("Digite um valor válido!")
            except ValueError as error:
                print("Digite um valor válido!")
                print(error)

    def menu(self):
        if self.__macaco1["nome"] == "" and self.__macaco2["nome"] == "":
            self.setNome()
        else:
            pass
        while True:
            print("1 - Comer \n2 - Ver Bucho\n3 - Digerir Comida\n4 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    self.comer()
                elif opcao == 2:
                    self.verBucho()
                elif opcao == 3:
                    self.digerirComida()
                elif opcao == 4:
                    exit("Até mais!")
                else:
                    print("Digite um valor válido!")
            except ValueError as error:
                print("Digite um valor válido!")
                print(error)

macacoStart = Macaco()
macacoStart.menu()