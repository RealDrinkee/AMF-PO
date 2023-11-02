from abc import ABC, abstractmethod


class Emprestar(ABC):
    @abstractmethod
    def emprestar(self):
        pass
    @abstractmethod
    def devolver(self):
        pass
class Material:

    def __init__(self, titulo, autor, editor, data_pub):
        self.titulo = titulo
        self.autor = autor
        self.editor = editor
        self.data_pub = data_pub


class Livros(Material, Emprestar):

    def __init__(self, titulo, autor, editor, data_pub):
        super().__init__(titulo, autor, editor, data_pub)
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"Emprestado: {self.titulo}")
        else:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")
        else:
            print(f"Não emprestado: {self.titulo}")

class Revistas(Material, Emprestar):

    def __init__(self, titulo, autor, editor, data_pub):
        super().__init__(titulo, autor, editor, data_pub)
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"Emprestado: {self.titulo}")
        else:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")

    def devolver (self):
        if self.emprestado:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")
        else:
            print(f"Não emprestado: {self.titulo}")
class Artigos(Material, Emprestar):

    def __init__(self, titulo, autor, editor, data_pub):
        super().__init__(titulo, autor, editor, data_pub)
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"Emprestado: {self.titulo}")
        else:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"Devolvido: {self.titulo}")
        else:
            print(f"Não emprestado: {self.titulo}")

if __name__ == "__main__":
    livro = Livros("A Arte da Guerra", "Sun Tzu", "Editora X", "2000")
    livro.emprestar()
    livro.devolver()
    revista = Revistas("Revista X", "Autor X", "Editora X", "2000")
    revista.emprestar()
    revista.devolver()
    artigo = Artigos("Artigo X", "Autor X", "Editora X", "2000")
    artigo.emprestar()
    artigo.devolver()

