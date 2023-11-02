class Numeros():

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

class Divisao(Numeros):

    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def dividir(self):
        try:
            if self.n2 == 0 or self.n1 == 0:
                raise ZeroDivisionError("Não é possível dividir por zero")
            return self.n1 / self.n2
        except ZeroDivisionError as error:
            print(error)
        except ValueError:
            print("Apenas números são aceitos")
        except Exception as error:
            print("Erro sem tratamento contate o suporte: ", error)

class Main(Divisao):

    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def main(self):
        while True:
            try:
                self.n1 = int(input("Digite o primeiro número: "))
                self.n2 = int(input("Digite o segundo número: "))
                resultado = self.dividir()
                if resultado is not None:
                    print(f"Resultado: {resultado}")
                break
            except ValueError:
                print("Apenas números são aceitos")
            except Exception as error:
                print("Erro sem tratamento contate o suporte: ", error)

if __name__ == "__main__":
    main = Main(0, 0)
    main.main()