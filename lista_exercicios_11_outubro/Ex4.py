from abc import ABC, abstractmethod

class ErrorMenuDeEscolha(Exception):
    pass

class Personagem(ABC):

    def __init__(self):
        self.dados = {
            "nome": "",
            "vida": 100,
            "ataque": 0,
            "defesa": 0,
            "velocidade": 0,
            "escolha_personagem": 0,
            "arma": ""
        }

    @abstractmethod
    def escolha_personagem(self):
        pass

    @abstractmethod
    def escolha_arma(self):
        pass

    def mostrar_status(self):
        print(f"Status de {self.dados['nome']} - Vida: {self.dados['vida']}, Ataque: {self.dados['ataque']}, Defesa: {self.dados['defesa']}")

class Monstro(ABC):

    def __init__(self):
        self.dados = {
            "nome": "",
            "vida": 100,
            "ataque": 0,
            "defesa": 0,
            "velocidade": 0,
            "arma": ""
        }

    @abstractmethod
    def escolha_monstro(self):
        pass

    @abstractmethod
    def escolha_arma(self):
        pass

    def mostrar_status(self):
        print(f"Status de {self.dados['nome']} - Vida: {self.dados['vida']}, Ataque: {self.dados['ataque']}, Defesa: {self.dados['defesa']}")

class EscolhaMonstro(Monstro):

    def escolha_monstro(self):
        print(f"Olá {self.dados['nome']}!")
        print("Escolha seu monstro: ")
        print("1 - Orc\n2 - Troll\n3 - Goblin")
        self.dados['escolha_personagem'] = int(input("Escolha seu monstro: "))

    def escolha_arma(self):
        print(f"{self.dados['nome']}, agora escolha sua arma de monstro.")
        while True:
            escolha = self.escolha_arma_validacao()
            try:
                if self.dados['escolha_personagem'] == 1:
                    if escolha == 1:
                        print("Você escolheu a Espada!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 5
                        self.dados['arma'] = "Espada"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu o Machado!")
                        self.dados['ataque'] += 15
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Machado"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu a Lança!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Lança"
                        return self.dados
                elif self.dados['escolha_personagem'] == 2:
                    if escolha == 1:
                        print("Você escolheu o Cajado!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 5
                        self.dados['arma'] = "Cajado"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu a Varinha!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Varinha"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu o Livro de Magia!")
                        self.dados['ataque'] += 2
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Livro de Magia"
                        return self.dados
                elif self.dados['escolha_personagem'] == 3:
                    if escolha == 1:
                        print("Você escolheu o Arco!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Arco"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu a Besta!")
                        self.dados['ataque'] += 15
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Besta"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu a Adaga!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Adaga"
                        return self.dados
                else:
                    raise ErrorMenuDeEscolha
            except ValueError:
                print("Opção inválida")
            except ErrorMenuDeEscolha:
                print("Opção inválida")

    def escolha_arma_validacao(self):
        if self.dados['escolha_personagem'] == 1:
            print("1 - Espada\n2 - Machado\n3 - Lança")
        elif self.dados['escolha_personagem'] == 2:
            print("1 - Cajado\n2 - Varinha\n3 - Livro de Magia")
        elif self.dados['escolha_personagem'] == 3:
            print("1 - Arco\n2 - Besta\n3 - Adaga")
        self.opcao = int(input("Escolha sua arma: "))
        return self.opcao

class EscolhaPersonagem(Personagem):

    def escolha_personagem(self):
        print(f"Olá {self.dados['nome']}!")
        print("Escolha seu personagem: ")
        print("1 - Guerreiro\n2 - Mago\n3 - Arqueiro")
        self.dados['escolha_personagem'] = int(input("Escolha seu personagem: "))

    def escolha_arma(self):
        print(f"{self.dados['nome']}, agora escolha sua arma de personagem.")
        while True:
            escolha = self.escolha_arma_validacao()
            try:
                if self.dados['escolha_personagem'] == 1:
                    if escolha == 1:
                        print("Você escolheu a Espada!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 5
                        self.dados['arma'] = "Espada"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu o Machado!")
                        self.dados['ataque'] += 15
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Machado"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu a Lança!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Lança"
                        return self.dados
                elif self.dados['escolha_personagem'] == 2:
                    if escolha == 1:
                        print("Você escolheu o Cajado!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 5
                        self.dados['arma'] = "Cajado"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu a Varinha!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Varinha"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu o Livro de Magia!")
                        self.dados['ataque'] += 2
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Livro de Magia"
                        return self.dados
                elif self.dados['escolha_personagem'] == 3:
                    if escolha == 1:
                        print("Você escolheu o Arco!")
                        self.dados['ataque'] += 10
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Arco"
                        return self.dados
                    elif escolha == 2:
                        print("Você escolheu a Besta!")
                        self.dados['ataque'] += 15
                        self.dados['defesa'] += 2
                        self.dados['arma'] = "Besta"
                        return self.dados
                    elif escolha == 3:
                        print("Você escolheu a Adaga!")
                        self.dados['ataque'] += 5
                        self.dados['defesa'] += 10
                        self.dados['arma'] = "Adaga"
                        return self.dados
                else:
                    raise ErrorMenuDeEscolha
            except ValueError:
                print("Opção inválida")
            except ErrorMenuDeEscolha:
                print("Opção inválida")

    def escolha_arma_validacao(self):
        if self.dados['escolha_personagem'] == 1:
            print("1 - Espada\n2 - Machado\n3 - Lança")
        elif self.dados['escolha_personagem'] == 2:
            print("1 - Cajado\n2 - Varinha\n3 - Livro de Magia")
        elif self.dados['escolha_personagem'] == 3:
            print("1 - Arco\n2 - Besta\n3 - Adaga")
        self.opcao = int(input("Escolha sua arma: "))
        return self.opcao

class MenuEscolhaPersonagem:

    def escolher_lado(self):
        print("1 - Bem\n2 - Mal")
        self.opcao = int(input("Escolha um lado: "))
        return self.opcao

    def escolher_personagem(self):
        if self.opcao == 1:
            print("Você escolheu o lado do Bem!")
            personagem = EscolhaPersonagem()
            personagem.dados['nome'] = input("Digite seu nome: ")
            personagem.escolha_personagem()
            personagem.escolha_arma()
            personagem.mostrar_status()

        elif self.opcao == 2:
            print("Você escolheu o lado do Mal!")
            monstro = EscolhaMonstro()
            monstro.dados['nome'] = input("Digite o nome do monstro: ")
            monstro.escolha_monstro()
            monstro.escolha_arma()
            monstro.mostrar_status()

        else:
            print("Opção inválida")

if __name__ == "__main__":
    menu = MenuEscolhaPersonagem()
    menu.escolher_lado()
    menu.escolher_personagem()
