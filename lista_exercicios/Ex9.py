# Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:
# 1. Possua uma classe chamada Ponto, com os atributos x e y.
# 2. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# 3. Possua uma função para imprimir os valores da classe Ponto
# 4. Possua uma função para encontrar o centro de um Retângulo.
# 5. Você deve criar alguns objetos da classe Retangulo.
# 6. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
# retângulo, que deve ser um objeto da classe Ponto.
# 7. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
# ponto que indique os valores de x e y para o centro do objeto.
# 8. O valor do centro do objeto deve ser mostrado na tela
# 9. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto():

    def __init__(self):
        self.__x = 0
        self.__y = 0

    def setX(self):
        self.__x = int(input("Digite o valor de X: "))
        return self.__x

    def setY(self):
        self.__y = int(input("Digite o valor de Y: "))
        return self.__y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


class Retangulo():

    def __init__(self):
        self.__largura = 0
        self.__altura = 0
        self.__ponto = Ponto()

    def setLargura(self):
        self.__largura = int(input("Digite a largura do retângulo: "))
        return self.__largura

    def setAltura(self):
        self.__altura = int(input("Digite a altura do retângulo: "))
        return self.__altura

    def getLargura(self):
        return self.__largura

    def getAltura(self):
        return self.__altura

    def getPonto(self):
        return self.__ponto

    def imprimirPonto(self):
        print(f"O ponto é: {self.__ponto.getX()}, {self.__ponto.getY()}")

    def centroRetangulo(self):
        centro = Ponto()
        centro.setX()
        centro.setY()
        return centro

    def imprimirCentro(self):
        print(f"O centro do retângulo é: {self.centroRetangulo().getX()}, {self.centroRetangulo().getY()}")

    def menu(self):
        while True:
            print("1 - Alterar valores do retângulo")
            print("2 - Imprimir centro do retângulo")
            print("3 - Sair")
            opcao = int(input("Digite a opção desejada: "))
            try:
                if opcao == 1:
                    self.setLargura()
                    self.setAltura()
                    self.getPonto().setX()
                    self.getPonto().setY()
                    self.menu()
                elif opcao == 2:
                    self.imprimirCentro()
                    self.menu()
                elif opcao == 3:
                    print("Saindo...")
                    exit()
                else:
                    print("Digite um valor válido!")
            except ValueError as error:
                print("Digite um valor válido!")
                print(error)

retangulo = Retangulo()
retangulo.menu()
