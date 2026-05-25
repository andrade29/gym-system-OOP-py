from entidades.pessoa import Pessoa

class Aluno(Pessoa): #subclasse Aluno

    def __init__(self, matricula: int, nome: str, data: str, cpf: str, sexo: str):
        super().__init__(nome, data, cpf, sexo)
        self.matricula = matricula

    def __str__(self): 
        return f'Aluno | Matrícula: {self.matricula}, {super().__str__()}'

    def fazer_Matricula(self):
        pass

    def cancelar_Matricula(self):
        pass

    def consultar_Treino(self):
        pass