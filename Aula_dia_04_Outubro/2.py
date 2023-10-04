class Animal():

    def __init__(self, nome):
        self.nome = nome

    def som(self):
        print("Emitir som genérico")


class Cachorro(Animal):

    def som(self):
        return "Wufff! Wufff!"

class Gato(Animal):

        def som(self):
            return "Meow! Meow!"

class Pato(Animal):

    def som(self):
        return "Quack! Quack!"


def fazer_um_som(self):
    print(f"{self.nome} faz: {self.som()}")


rex = Cachorro("Rex")
whiskers = Gato("Whiskers")
donald = Pato("Donald")

fazer_um_som(rex)
fazer_um_som(whiskers)
fazer_um_som(donald)