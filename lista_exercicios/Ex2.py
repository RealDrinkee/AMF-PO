# Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado():
    def __init__(self):
        self.lado = 0

    def mudarLado(self):
        self.lado = int(input("Digite o valor do lado: "))
        self.calcularArea()
        return self.lado

    def calcularArea(self):
        print(f"A área do quadrado é de {self.lado ** 2} cm²")


quadrado = Quadrado()
quadrado.mudarLado()

