from abc import ABC, abstractmethod

class Evento(ABC):
    def __init__(self, nome, data, local, preco):
        self.nome = nome
        self.data = data
        self.local = local
        self.preco = preco

    @abstractmethod
    def custo(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}\nData: {self.data}\nLocal: {self.local}\nPreço: {self.preco}"

class Palestra(Evento):
    def __init__(self, nome, data, local, preco, palestrante, cachet):
        super().__init__(nome, data, local, preco)
        self.palestrante = palestrante
        self.cachet = cachet

    def custo(self):
        return self.preco + self.cachet

    def __str__(self):
        return super().__str__() + f"\nPalestrante: {self.palestrante}\nCachet: {self.cachet}"

class Workshop(Evento):
    def __init__(self, nome, data, local, preco, instrutor, custo_material):
        super().__init__(nome, data, local, preco)
        self.instrutor = instrutor
        self.custo_material = custo_material

    def custo(self):
        return self.preco + self.custo_material

    def __str__(self):
        return super().__str__() + f"\nInstrutor: {self.instrutor}\nCusto Material: {self.custo_material}"

class Conferencia(Evento):
    def __init__(self, nome, data, local, preco, palestrante, cachet, instrutor, custo_material):
        super().__init__(nome, data, local, preco)
        self.palestrante = palestrante
        self.cachet = cachet
        self.instrutor = instrutor
        self.custo_material = custo_material

    def custo(self):
        return self.preco + self.cachet + self.custo_material

    def __str__(self):
        return super().__str__() + f"\nPalestrante: {self.palestrante}\nCachet: {self.cachet}\nInstrutor: {self.instrutor}\nCusto Material: {self.custo_material}"


palestra = Palestra("Palestra", "02/02/2022", "Local da Palestra", 50, "Palestrante 1", 20)
print("Dados da Palestra:")
print(palestra)
print("Custo da Palestra:", palestra.custo())
print()

workshop = Workshop("Workshop", "03/03/2022", "Local do Workshop", 80, "Instrutor 1", 30)
print("Dados do Workshop:")
print(workshop)
print("Custo do Workshop:", workshop.custo())
print()

conferencia = Conferencia("Conferencia", "04/04/2022", "Local da Conferencia", 150, "Palestrante 2", 40, "Instrutor 2", 50)
print("Dados da Conferencia:")
print(conferencia)
print("Custo da Conferencia:", conferencia.custo())
