class Produto:
    def __init__(self, nome, preco):
      self.nome = nome
      self.preco = preco

    def mostrar_info(self):
       print(f"Produto: - {self.nome} - Preço: {self.preco}")


class ProdutoDigital(Produto):
   def __init__(self, nome, preco, tamanho_mb):
      super().__init__(nome, preco)
      self.tamanho_mb = tamanho_mb

def mostrar_info(self):
      super().mostrar_info()
      print(f"Tamanho: {self.tamanho_mb} MB")

jogo_fifa = ProdutoDigital("FIFA", 300.0, 2000)
jogo_fifa.mostrar_info()

      


