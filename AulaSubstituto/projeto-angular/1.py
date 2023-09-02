# Quero fazer uma lista sem usar listas ou funções de listas e sem parenteses


class Lista:
  def __init__(self, *args):
    self.lista = args

  def __str__(self):
    return str(self.lista)


  def __getitem__(self, index):
    return self.lista[index]

  

