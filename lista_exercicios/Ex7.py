# Classe Bichinho Virtual: Crie uma classe que modele um Tamagotchi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade;
# Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em
# consideração, o Humor do nosso Tamagotchi, este humor é uma combinação entre os atributos
# Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para
# armazenar esta informação por que ela pode ser calculada a qualquer momento.

# class verificarFome():
#
#     def __init__(self):
#         self.atributoExterno = Tamagotchi()
#
#
#     def obter__Atributo(self):
#         print(self.atributoExterno.fome)
#         return self.atributoExterno.fome

class Tamagotchi():

    def __init__(self):
        self.nome = ""
        self.fome = 0
        self.saude = 0
        self.idade = 0
        self.humor = 0

    def setNome(self):
        self.nome = input("Qual o nome do seu Tamagotchi? ")
        return self.nome

    def setFome(self):
        opcao = 0
        while opcao != 6:
            print("1 - Maça +2 \n2 - Banana + 5\n3 - Pera + 3\n4 - Uva + 1\n5 - Melancia + 10\n6 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    print("Você deu uma maça para o seu Tamagotchi")
                    self.fome += 2
                    self.saude += 1
                    print(f"Você aumentou a saúde do seu Tamagotchi em +1: {self.saude}")
                    self.voltarMenu()

                elif opcao == 2:
                    print("Você deu uma banana para o seu Tamagotchi")
                    self.fome += 5
                    self.saude += 1
                    print(f"Você aumentou a saúde do seu Tamagotchi em +1: {self.saude}")
                    self.humor += 5
                    print(f"Você aumentou o humor do seu Tamagotchi em +5: {self.humor}")
                    self.voltarMenu()

                elif opcao == 3:
                    print("Você deu uma pera para o seu Tamagotchi")
                    self.fome += 3
                    self.saude += 1
                    print(f"Você aumentou a saúde do seu Tamagotchi em +1: {self.saude}")
                    self.voltarMenu()

                elif opcao == 4:
                    print("Você deu uma uva para o seu Tamagotchi")
                    self.fome += 1
                    self.saude += 1
                    print(f"Você aumentou a saúde do seu Tamagotchi em +1: {self.saude}")
                    self.voltarMenu()

                elif opcao == 5:
                    print("Você deu uma melancia para o seu Tamagotchi")
                    self.fome += 10
                    self.humor += 10
                    print(f"Você aumentou o humor do seu Tamagotchi em +5: {self.humor}")
                    self.saude += 2
                    print(f"Você aumentou a saúde do seu Tamagotchi em +2: {self.saude}")
                    self.voltarMenu()

                elif opcao == 6:
                    print("Até mais!")
                    break
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)
        return opcao, self.fome, self.saude, self.humor

    def setSaude(self):
        print("1 - Remédio +2 \n2 - Vacina + 5\n3 - Sair")
        opcao = int(input("Qual opção deseja? "))
        while opcao != 3:
            try:
                if opcao == 1:
                    print("Você deu um remédio para o seu Tamagotchi")
                    self.saude += 2
                    print(f"Você aumentou a saúde do seu Tamagotchi em +2: {self.saude}")
                elif opcao == 2:
                    print("Você deu uma vacina para o seu Tamagotchi")
                    self.saude += 5
                    print(f"Você aumentou a saúde do seu Tamagotchi em +5: {self.saude}")
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)
        return opcao, self.saude

    def setIdade(self):
        self.idade += 1
        print(f"Seu Tamagotchi está com {self.idade} anos")
        return self.idade

    def brincar(self):
        if self.fome <= 5:
            print("Seu Tamagotchi está com fome, alimente-o antes de brincar")
            self.setFome()
        else:
            self.Verificar
            pass
        opcao = 0
        while opcao != 3:
            print("1 - Jogar bola +2 \n2 - Passear + 5\n3 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    print("Você jogou bola com o seu Tamagotchi")
                    self.humor += 2
                    self.fome -= 4
                    print(f"Você aumentou o humor do seu Tamagotchi em +2: {self.humor}")
                elif opcao == 2:
                    print("Você passeou com o seu Tamagotchi")
                    self.humor += 5
                    self.fome -= 10
                    print(f"Você aumentou o humor do seu Tamagotchi em +5: {self.humor}")
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)

        return opcao, self.humor


    def voltarMenu(self):
        opcao = 0
        while opcao != 2:
            print("1 - Voltar ao menu\n2 - Retornar")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    self.main()
                elif opcao == 2:
                    break
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)
        return opcao
    def main(self):
        opcao = 0
        while opcao != 6:
            print("1 - Mudar nome\n2 - Alimentar\n3 - Dar remédio\n4 - Brincar\n5 - Status do Tamagotchi\n6 - Sair")
            opcao = int(input("Qual opção deseja? "))
            try:
                if opcao == 1:
                    self.setNome()
                elif opcao == 2:
                    self.setFome()
                elif opcao == 3:
                    self.setSaude()
                elif opcao == 4:
                    self.brincar()
                elif opcao == 5:
                    print(f"Nome: {self.nome}\nFome: {self.fome}\nSaúde: {self.saude}\nIdade: {self.idade}\nHumor: {self.humor}")
                elif opcao == 6:
                    print("Até mais")
                    break
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)

game = Tamagotchi()
game.main()


