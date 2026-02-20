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
class Filho(Pai, Mae):
    def __init__(self):
        super().__init__()

        #Criando uma instância temporária para extrair o valor da classe mae
        instancia_mae = Mae()
        self.cor_olhos = instancia_mae.cor_olhos # Forçando a herança da mãe

    #Metodo
    def mostrar_origem(self):
        print(f"Sobrenome: {self.sobrenome} ")
        print(f"Cor dos olhos: {self.cor_olhos} ")
        print(f"Ação: {self.falar()} ")
              
#Teste do sistema
crianca = Filho() # Criei um objeto

#Como acessar os métodos do meu objeto crianca?
crianca.mostrar_origem() 


# Ordem de resolução de métodos MRO
for classe in Filho.mro():
    print(classe) 