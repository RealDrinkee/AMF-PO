# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle
# deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis
# que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira.
# Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos
# (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).
# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de
# fome e tédio.
import random


class ColheitaFeliz():

    def __init__(self):
        self.__todos__animais = {
            "lista__de__animais": ["Vaca", "Cavalo", "Galinha", "Porco", "Ovelha", "Cabra", "Pato", "Coelho", "Gato", "Cachorro"],
            "nivel_dos_animais": [random.randint(0, 30) for _ in range(10)],
            "fome__dos__animais": [random.randint(0, 30) for _ in range(10)],
            "humor__dos__animais": [random.randint(0, 30) for _ in range(10)],
        }


    def getTodosAnimais(self):
        return self.__todos__animais

    def alimentar_todos_animais(self):
        for i in range(len(self.__todos__animais["lista__de__animais"])):
            self.__todos__animais["fome__dos__animais"][i] += 5
        return self.__todos__animais["fome__dos__animais"]

    def brincar_com_todos_animais(self):
        for i in range(len(self.__todos__animais["lista__de__animais"])):
            self.__todos__animais["humor__dos__animais"][i] += 5
        return self.__todos__animais["humor__dos__animais"]

    def ouvir_todos_animais(self):
        for i in range(len(self.__todos__animais["lista__de__animais"])):
            self.__todos__animais["nivel_dos_animais"][i] += 5
        return self.__todos__animais["nivel_dos_animais"]

    def status_todos_os_animais_organizado(self):
        for i in range(len(self.__todos__animais["lista__de__animais"])):
            print(f"O animal {self.__todos__animais['lista__de__animais'][i]} está com o nível {self.__todos__animais['nivel_dos_animais'][i]}, fome {self.__todos__animais['fome__dos__animais'][i]} e humor {self.__todos__animais['humor__dos__animais'][i]}")



    def menu(self):
        print("1 - Alimentar todos os animais\n2 - Brincar com todos os animais\n3 - Ouvir todos os animais\n4 - Status dos animais\n5 - Sair")
        opcao = int(input("Qual opção deseja? "))
        return opcao

    def main(self):
        while True:
            opcao = self.menu()
            try:
                if opcao == 1:
                    print(f"O nível de fome dos animais é: {self.alimentar_todos_animais()}")
                elif opcao == 2:
                    print(f"O humor dos animais é: {self.brincar_com_todos_animais()}")
                elif opcao == 3:
                    print(f"O nível dos animais é: {self.ouvir_todos_animais()}")
                elif opcao == 4:
                    self.status_todos_os_animais_organizado()
                elif opcao == 5:
                    print("Saindo...")
                    exit()
                else:
                    print("Digite um valor válido!")
            except ValueError:
                print("Caracter inválido!")

animais = ColheitaFeliz()
animais.main()