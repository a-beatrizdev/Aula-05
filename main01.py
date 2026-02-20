# Herança múltipla

class Pai:
    def __init__(self):
        self.sobrenome = "Silva"
        self.cor_olhos = "Castanhos"

    def falar(self):
        return "O pai está falando"
    
class Mae:
    def __init__(self):
        self.sobrenome = "Oliveira"
        self.cor_olhos = "Azuis"

    def falar(self):
        return "A mãe está falando"
    
# Criando a subclasse com herança
#A classe filho herda de pai
class Filho(Pai):
    def __init__(self):
        super().__init__()

    #Metodo
    def mostrar_origem(self):
        print(f"Sobrenome: {self.sobrenome} ")
        print(f"Cor dos olhos: {self.cor_olhos} ")
        print(f"Sobrenome: {self.sobrenome} ")
              
   