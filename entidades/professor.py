from entidades.pessoa import Pessoa

class Professor(Pessoa): #subclasse Professor

    def __init__(self, cref: str, nome: str, data: str, cpf: str, sexo: str):
        super().__init__(nome, data, cpf, sexo)
        self.cref = cref 

    def __str__(self):
        return f'Professor | CREF: {self.cref}, {super().__str__()}'
    
    def consultar_Aluno(self):
        pass

    def criar_Treino(self):
        pass