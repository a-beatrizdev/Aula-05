class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def exibir_dados(self):
        print(f"Pessoa: - {self.nome} - cpf: {self.cpf}")

    def saudacao(self):
        return f"Olá, meu nome é João e meu cpf é {self.cpf}"
    
class Aluno(Pessoa):
    def __init__(self, nome, cpf, ra_aluno):
        super().__init__(nome, cpf)
        self.ra_aluno = ra_aluno 

    def exibir_dados(self):
        super().exibir_dados()
        print(f"RA: - {self.ra_aluno} ra")

class Professor(Pessoa):
    def __init__(self, nome, cpf, )











