# Classe Retangulo: Crie uma classe que modele um retangulo:
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de
# um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
# rodapés necessárias para o local.

class Retangulo():
    def __init__(self):
        self.ladoA = 0
        self.ladoB = 0

    def atributos(self):
        self.ladoA = float(input("Digite o valor do lado A: "))
        self.ladoB = float(input("Digite o valor do lado B: "))
        return self.ladoA, self.ladoB

    def calcularArea(self):
        print(f"A área do retângulo é de {self.ladoA * self.ladoB} cm²")

    def calcularPerimetro(self):
        print(f"O perímetro do retângulo é de {2 * (self.ladoA + self.ladoB)} cm")

    def main(self):
        self.atributos()
        self.calcularArea()
        self.calcularPerimetro()

retangulo = Retangulo()
retangulo.main()
