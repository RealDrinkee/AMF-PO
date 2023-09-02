# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário
# deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de
# que o número do canal e o nível do volume permanecem dentro de faixas válidas.

class TV():
    def __init__(self):
        self.canal = 0
        self.volume = 0

    def setCanal(self):
        self.canal = int(input("Qual canal deseja assistir? "))
        if self.canal < 0 or self.canal > 100:
            print("Canal inválido")
            self.setCanal()
        else:
            print(f"Você está assistindo o canal {self.canal}")
        return self.canal

    def setVolume(self):
        self.volume = int(input("Qual volume deseja? "))
        if self.volume < 0 or self.volume > 100:
            print("Volume inválido")
            self.setVolume()
        else:
            print(f"O volume está em {self.volume}")
        return self.volume

    def tvStatus(self):
        print(f"Você está assistindo o canal {self.canal} com o volume em {self.volume}")

    def menu(self):
        print("1 - Mudar canal\n2 - Mudar volume\n3 - Status da TV\n4 - Sair")
        opcao = int(input("Qual opção deseja? "))
        return opcao

    def main(self):
        while True:
            opcao = self.menu()
            try:
                if opcao == 1:
                    self.setCanal()
                elif opcao == 2:
                    self.setVolume()
                elif opcao == 3:
                    self.tvStatus()
                elif opcao == 4:
                    break
                else:
                    print("Opção inválida")
            except BaseException as ex:
                print("Erro: ", ex)
classTV = TV()
classTV.main()
