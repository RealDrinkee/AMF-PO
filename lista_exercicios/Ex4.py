# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhecer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa
# pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa():
    def __init__(self):
        self.nome = None
        self.idade = None
        self.peso = None
        self.altura = None

    def atributos(self):
        self.nome = input("Digite o nome: ")
        self.idade = int(input("Digite a idade: "))
        self.peso = float(input("Digite o peso: "))
        self.altura = float(input("Digite a altura: "))
        return self.nome, self.idade, self.peso, self.altura

    def envelhecer(self):
        if self.idade < 21:
            self.idade += 1
            self.crescer()
        else:
            print("Você já é maior de idade")
        return self.idade

    def engordar(self):
        self.peso += 1
        return self.peso

    def emagrecer(self):
        self.peso -= 1
        return self.peso
    def crescer(self):
        if self.idade < 21:
            self.altura += 0.5
        return self.altura

    def mostrarAtributos(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}")

    def menu(self):
        print("1 - Envelhecer\n2 - Engordar\n3 - Emagrecer\n4 - Crescer\n5 - Mostrar Atributos\n6 - Sair")
        escolha = int(input("Escolha uma opção: "))
        return escolha

    def main(self):
        while True:
            escolha = self.menu()
            if not self.nome or not self.idade or not self.peso or not self.altura:
                self.atributos()
            else:
                try:
                    if escolha == 1:
                        self.envelhecer()
                    elif escolha == 2:
                        self.engordar()
                    elif escolha == 3:
                        self.emagrecer()
                    elif escolha == 4:
                        self.crescer()
                    elif escolha == 5:
                        self.mostrarAtributos()
                    elif escolha == 6:
                        break
                    else:
                        print("Opção inválida")
                except ValueError:
                    print("Valor inválido")
                except BaseException as ex:
                    print("Erro:", ex)

pessoa = Pessoa()
pessoa.main()

