# Herança

#Criando uma classe SuperClasse (Pai ou mãe)
class Veiculo:
    #Criando os atributos
    def __init__(self, marca, qtd_marcha, modelo, qtd_rodas):
        self.marca = marca
        self.marcha = qtd_marcha 
        self.modelo = modelo
        self.rodas = qtd_rodas

    #Criando métodos da classe veiculo
    def mostrar_info(self):
        print(f"Marca: {self.marca} - Modelo: {self.modelo} - Marcha: {self.marcha} - Rodas {self.rodas}")


#subclasse ou Classe filho
class Carro(Veiculo):
    def __init__(self, marca, qtd_marcha, modelo, qtd_rodas, portas):
        # A função super é usada para herdar os atributos da classe pai
        super().__init__(marca, qtd_marcha, modelo, qtd_rodas)
        self.portas = portas

    
#Criando o objeto
meu_carro = Carro("Tesla", 6, "Cybertruck", 4, 4) 

