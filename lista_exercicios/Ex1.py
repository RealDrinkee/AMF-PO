class Bola():
    def __init__(self):
        self.cor = ""
        self.circunferencia = 0
        self.material = ""
        self.raio = 0

    def menu(self):
        print("1 - Trocar cor")
        print("2 - Mostrar Atributos")
        print("3 - Atributos")
        print("4 - Sair")
        escolha = int(input("Escolha uma opção: "))
        return escolha

    def trocaCor(self):
        self.cor = input("Digite a cor: ")
        return self.cor

    def mostrarAtributos(self):
        print(f"Cor: {self.cor}\nCircunferência: {self.circunferencia}\nMaterial: {self.material}\nRaio: {self.raio}")
    def atributos(self):
        self.cor = input("Digite a cor: ")
        self.raio = float(input("Insira o raio da bola de futebol: "))
        self.material = input("Digite o material: ")
        self.circunferencia = float(input("Digite a circunferência: "))
        return self.cor, self.circunferencia, self.material, self.raio

    def circunferenciaCalc(self):
        pi = 3.14159
        print(f"A circunferência da bola de futebol é de {self.circunferencia:.2f} cm.")
        return 2 * pi * self.raio

    def main(self):
        while True:
            escolha = self.menu()
            try:
                if escolha == 1:
                    self.trocaCor()
                elif escolha == 2:
                    self.mostrarAtributos()
                elif escolha == 3:
                    self.atributos()
                    self.circunferenciaCalc()
                elif escolha == 4:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Valor inválido")
            except BaseException as ex:
                print("Erro:", ex)


bola = Bola()
bola.main()
