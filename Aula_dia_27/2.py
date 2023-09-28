class aluno_g:

    def __init__(self):
        self.__nome = ""
        self.__g1 = 0
        self.__g2 = 0
        self.___g3 = 0
        self.__media = 0
        
    def set_nome(self, nome):
        self.__nome = nome

    def set_notas(self, g1, g2, g3):
        self.__g1 = g1
        self.__g2 = g2
        self.__g3 = g3

    def escolher_notas(self):
        g1 = float(input("Digite a nota da G1: "))
        g2 = float(input("Digite a nota da G2: "))
        g3 = float(input("Digite a nota da G3: "))
        return g1, g2, g3

    def calcular_media(self):
        self.__media = (self.__g1 + self.__g2 + self.__g3) / 3
        return self.__media
    

    def print_dados(self):
        print(f"Nome: {self.__nome}\nG1: {self.__g1}\nG2: {self.__g2}\nG3: {self.__g3}\nMédia: {self.__media}")


    @staticmethod
    def main_aluno_g():
        aluno = aluno_g()
        aluno.set_nome(input("Digite o nome do aluno: "))
        g1, g2, g3 = aluno.escolher_notas()
        aluno.set_notas(g1, g2, g3)
        aluno.calcular_media()
        aluno.print_dados()

class aluno_p:

    def __init__(self):
        self.__nome = ""
        self.__g1 = 0
        self.__g2 = 0
        self.___g3 = 0
        self.__g4 = 0
        self.__media = 0

    def set_nome(self, nome):
        self.__nome = nome

    def set_notas(self, g1, g2, g3, g4):
        self.__g1 = g1
        self.__g2 = g2
        self.__g3 = g3
        self.__g4 = g4

    def escolher_notas(self):
        g1 = float(input("Digite a nota da G1: "))
        g2 = float(input("Digite a nota da G2: "))
        g3 = float(input("Digite a nota da G3: "))
        g4 = float(input("Digite a nota da G4: "))
        return g1, g2, g3, g4
    
    def calcular_media(self, g1, g2, g3, g4):
        self.__media = (self.__g1 + self.__g2 + self.__g3 + self.__g4) / 4
        return self.__media
    
    def print_dados(self):
        print(f"Nome: {self.__nome}\nG1: {self.__g1}\nG2: {self.__g2}\nG3: {self.__g3}\nG4: {self.__g4}\nMédia: {self.__media}")


    @staticmethod
    def main_aluno_p():
        aluno = aluno_p()
        aluno.set_nome(input("Digite o nome do aluno: "))
        g1, g2, g3, g4 = aluno.escolher_notas()
        aluno.set_notas(g1, g2, g3, g4)
        aluno.calcular_media()
        aluno.print_dados()




class Main:

    @staticmethod
    def main():

        while True:
            try:
                print("1 - Aluno de Graduação\n2 - Aluno de Pós-Graduação")
                escolha = int(input("Escolha uma opção: "))

                if escolha == 1:
                    aluno_g.main_aluno_g()

                elif escolha == 2:
                    aluno_p.main_aluno_p()

                elif escolha == 3:
                    break
                else:
                    print("Opção inválida")

            except ValueError:
                print("Valor inválido")


if __name__ == "__main__":
    Main.main()
