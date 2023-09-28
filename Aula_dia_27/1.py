class Calculadora():

    def __init__(self):
        self.__numero1 = 0
        self.__numero2 = 0

    def somar(self, numero1, numero2):

        soma = (numero1 + numero2)
        print(f"A soma dos números é: {soma}")

class escolher_numeros():

    def __init__(self):
        self.numero1 = 0 
        self.numero2 = 0


    def escolher_numeros(self):
        self.numero1 = int(input("Digite o primeiro número: "))
        self.numero2 = int(input("Digite o segundo número: "))
        
    def chamar_soma(self):
        self.escolher_numeros()
        objeto = Calculadora()
        objeto.somar(self.numero1, self.numero2)


b = escolher_numeros()
b.chamar_soma()


