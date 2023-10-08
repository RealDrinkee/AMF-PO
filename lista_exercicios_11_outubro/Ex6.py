# 6 - Simulação de Tráfego Rodoviário
#
# • Neste exercício, você criaria uma simulação de tráfego rodoviário onde
# diferentes tipos de veículos, como Carro, Caminhao e Moto, interagiriam na
# estrada.
# • Cada classe de veículo teria métodos para simular comportamentos de
# tráfego, como aceleração, frenagem, mudança de faixa,
# ultrapassagens, etc.
# • O polimorfismo permitiria que os veículos interagissem uns com os
# outros de maneira flexível, refletindo o comportamento real do
# tráfego.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.placa = placa

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def mudar_faixa(self):
        pass

    @abstractmethod
    def ultrapassar(self):
        pass

    def __str__(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}\nCor: {self.cor}\nPlaca: {self.placa}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor, placa, num_portas):
        super().__init__(marca, modelo, ano, cor, placa)
        self.num_portas = num_portas

    def acelerar(self):
        print("Carro acelerando")

    def frear(self):
        print("Carro freando")

    def mudar_faixa(self):
        print("Carro mudando de faixa")

    def ultrapassar(self):
        print("Carro ultrapassando")

    def __str__(self):
        return super().__str__() + f"\nNúmero de Portas: {self.num_portas}"

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cor, placa, num_eixos):
        super().__init__(marca, modelo, ano, cor, placa)
        self.num_eixos = num_eixos

    def acelerar(self):
        print("Caminhão acelerando")

    def frear(self):
        print("Caminhão freando")

    def mudar_faixa(self):
        print("Caminhão mudando de faixa")

    def ultrapassar(self):
        print("Caminhão ultrapassando")

    def __str__(self):
        return super().__str__() + f"\nNúmero de Eixos: {self.num_eixos}"

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cor, placa, cilindradas):
        super().__init__(marca, modelo, ano, cor, placa)
        self.cilindradas = cilindradas

    def acelerar(self):
        print("Moto acelerando")

    def frear(self):
        print("Moto freando")

    def mudar_faixa(self):
        print("Moto mudando de faixa")

    def ultrapassar(self):
        print("Moto ultrapassando")

    def __str__(self):
        return super().__str__() + f"\nCilindradas: {self.cilindradas}"

carro = Carro("Marca 1", "Modelo 1", 2021, "Cor 1", "Placa 1", 4)
print("Dados do Carro:")
print(carro)
carro.acelerar()
carro.frear()
carro.mudar_faixa()
carro.ultrapassar()
print()
caminhao = Caminhao("Marca 2", "Modelo 2", 2021, "Cor 2", "Placa 2", 6)
print("Dados do Caminhão:")
print(caminhao)
caminhao.acelerar()
caminhao.frear()
caminhao.mudar_faixa()
caminhao.ultrapassar()
print()
moto = Moto("Marca 3", "Modelo 3", 2021, "Cor 3", "Placa 3", 150)
print("Dados da Moto:")
print(moto)
moto.acelerar()
moto.frear()
moto.mudar_faixa()
moto.ultrapassar()
print()

