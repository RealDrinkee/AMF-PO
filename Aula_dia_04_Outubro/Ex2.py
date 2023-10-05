#Para desenvolver a classe teste que é apresentada a seguir e necessario criar tambem
#a classe Oficina que tera dois metodos:
#proximo() que retorna aleatoriamente um objeto do tipo bicicleta ou automovel
#manutencao(Veiculo v) que recebe como parametro um objetoo do tipo veiculo e chama
#os metodos definidos na classe veiculo
#listaVerificacoes()
#ajustar()
#limpar()
#se o veiculo for automovel deve tambem chamaro meoto mudarOleo()

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

class Oficina():
    def proximo(self):
        import random
        if random.randint(0,1) == 0:
            print("Caiu Bicicleta")
            return comum_bicicleta()
        else:
            print("Caiu Automovel")
            return comum_automovel()
    def manutencao(self, opc):
        opc.listarVerificacoes()
        opc.ajustar()
        opc.limpar()
        if isinstance(valor, comum_automovel):
            valor.mudarOleo()

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

    oficina = Oficina()
    v = oficina.proximo()