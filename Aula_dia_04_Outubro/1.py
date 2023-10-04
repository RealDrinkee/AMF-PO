class Mamifero():

    def som(self):
        print("Emitir som genérico")

class Homem():

    def som(self):
        print("Oi")

class Cachorro():

    def som(self):
        print("Wufff! Wufff!")


class Gato():

    def som(self):
        print("Meow! Meow!")


mami = Mamifero()
mami.som()

animais = [Homem(), Cachorro(), Gato()]
for animal in animais:
    animal.som()