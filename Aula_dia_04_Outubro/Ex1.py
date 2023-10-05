import abc
class veiculo_abstrato(abc.ABC):
    @abc.abstractmethod
    def listarVerificacoes(self):
        pass

    @abc.abstractmethod
    def ajustar(self):
        pass

    @abc.abstractmethod
    def limpar(self):
        pass

class comum_bicicleta(veiculo_abstrato):
    def listarVerificacoes(self):
        print("Verificar freios, pneus e marchas")
    def ajustar(self):
        print("Ajustar freios, pneus e marchas")
    def limpar(self):
        print("Limpar quadro, roda e corrente")

class comum_automovel(veiculo_abstrato):
    def listarVerificacoes(self):
        print("Verificar freios, pneus e motor")
    def ajustar(self):
        print("Ajustar freios, pneus e motor")
    def limpar(self):
        print("Limpar atribuicao_carroceria, rodas e motor")
    def mudarOleo(self):
        print("Trocar óleo do motor")

if __name__ == "__main__":
    atribuicao_bike = comum_bicicleta()
    atribuicao_bike.listarVerificacoes()
    atribuicao_bike.ajustar()
    atribuicao_bike.limpar()

    atribuicao_carro = comum_automovel()
    atribuicao_carro.listarVerificacoes()
    atribuicao_carro.ajustar()
    atribuicao_carro.limpar()
    atribuicao_carro.mudarOleo()