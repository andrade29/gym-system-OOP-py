class Pessoa:

    def __init__(self, nome: str, data: str, cpf: str, sexo: str): #classe-mãe pessoa
        self.nome = nome
        self.data = data
        self.cpf = cpf 
        self.sexo = sexo 

    def __str__(self):
        return f'{self.nome}, {self.data}, {self.cpf}, {self.sexo}'
    

    