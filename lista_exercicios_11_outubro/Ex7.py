# 7 - Sistema de Gerenciamento de Projetos
#
# • Neste exercício, você desenvolveria um sistema de gerenciamento de
# projetos, onde cada projeto é composto por várias tarefas e recursos.
# • As classes Projeto, Tarefa e Recurso seriam usadas para representar esses
# elementos.
# • O polimorfismo seria aplicado para calcular o progresso do projeto e a
# alocação de recursos de maneira flexível, permitindo que diferentes
# tipos de projetos e tarefas fossem gerenciados eficazmente.

from abc import ABC, abstractmethod

class Projeto(ABC):
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.tarefas = []

    @abstractmethod
    def progresso(self):
        pass

    @abstractmethod
    def alocar_recursos(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}\nData de Início: {self.data_inicio}\nData de Fim: {self.data_fim}"

class Tarefa(ABC):
    def __init__(self, nome, data_inicio, data_fim):
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    @abstractmethod
    def progresso(self):
        pass

    @abstractmethod
    def alocar_recursos(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}\nData de Início: {self.data_inicio}\nData de Fim: {self.data_fim}"

class Recurso(ABC):
    def __init__(self, nome, tipo):
        self.nome = nome
        self.tipo = tipo

    @abstractmethod
    def alocar(self):
        pass

    def __str__(self):
        return f"Nome: {self.nome}\nTipo: {self.tipo}"

class ProjetoSoftware(Projeto):
    def __init__(self, nome, data_inicio, data_fim, linguagem):
        super().__init__(nome, data_inicio, data_fim)
        self.linguagem = linguagem

    def progresso(self):
        print("Progresso do Projeto de Software")

    def alocar_recursos(self):
        print("Alocando Recursos para Projeto de Software")

    def __str__(self):
        return super().__str__() + f"\nLinguagem: {self.linguagem}"

class ProjetoHardware(Projeto):
    def __init__(self, nome, data_inicio, data_fim, tipo):
        super().__init__(nome, data_inicio, data_fim)
        self.tipo = tipo

    def progresso(self):
        print("Progresso do Projeto de Hardware")

    def alocar_recursos(self):
        print("Alocando Recursos para Projeto de Hardware")

    def __str__(self):
        return super().__str__() + f"\nTipo: {self.tipo}"

class TarefaSoftware(Tarefa):
    def __init__(self, nome, data_inicio, data_fim, linguagem):
        super().__init__(nome, data_inicio, data_fim)
        self.linguagem = linguagem

    def progresso(self):
        print("Progresso da Tarefa de Software")

    def alocar_recursos(self):
        print("Alocando Recursos para Tarefa de Software")

    def __str__(self):
        return super().__str__() + f"\nLinguagem: {self.linguagem}"

class TarefaHardware(Tarefa):
    def __init__(self, nome, data_inicio, data_fim, tipo):
        super().__init__(nome, data_inicio, data_fim)
        self.tipo = tipo

    def progresso(self):
        print("Progresso da Tarefa de Hardware")

    def alocar_recursos(self):
        print("Alocando Recursos para Tarefa de Hardware")

    def __str__(self):
        return super().__str__() + f"\nTipo: {self.tipo}"

class RecursoSoftware(Recurso):
    def __init__(self, nome, tipo, linguagem):
        super().__init__(nome, tipo)
        self.linguagem = linguagem

    def alocar(self):
        print("Alocando Recurso de Software")

    def __str__(self):
        return super().__str__() + f"\nLinguagem: {self.linguagem}"

class RecursoHardware(Recurso):
    def __init__(self, nome, tipo, tipo_hardware):
        super().__init__(nome, tipo)
        self.tipo_hardware = tipo_hardware

    def alocar(self):
        print("Alocando Recurso de Hardware")

    def __str__(self):
        return super().__str__() + f"\nTipo de Hardware: {self.tipo_hardware}"

projeto_software = ProjetoSoftware("Projeto de Software", "01/01/2022", "01/01/2023", "Python")
print("Dados do Projeto de Software:")
print(projeto_software)
projeto_software.progresso()
projeto_software.alocar_recursos()
print()
projeto_hardware = ProjetoHardware("Projeto de Hardware", "01/01/2022", "01/01/2023", "Arduino")
print("Dados do Projeto de Hardware:")
print(projeto_hardware)
projeto_hardware.progresso()
projeto_hardware.alocar_recursos()
print()
tarefa_software = TarefaSoftware("Tarefa de Software", "01/01/2022", "01/01/2023", "Python")
print("Dados da Tarefa de Software:")
print(tarefa_software)
tarefa_software.progresso()
tarefa_software.alocar_recursos()
print()
tarefa_hardware = TarefaHardware("Tarefa de Hardware", "01/01/2022", "01/01/2023", "Arduino")
print("Dados da Tarefa de Hardware:")
print(tarefa_hardware)
tarefa_hardware.progresso()
tarefa_hardware.alocar_recursos()
print()
recurso_software = RecursoSoftware("Recurso de Software", "Software", "Python")
print("Dados do Recurso de Software:")
print(recurso_software)
recurso_software.alocar()
print()
recurso_hardware = RecursoHardware("Recurso de Hardware", "Hardware", "Arduino")
print("Dados do Recurso de Hardware:")
print(recurso_hardware)
recurso_hardware.alocar()
print()