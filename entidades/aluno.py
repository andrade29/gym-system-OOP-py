from entidades.pessoa import Pessoa
from database.connection import Base
from sqlalchemy import Column, Integer, ForeignKey

class Aluno(Pessoa): #subclasse Aluno

    __tablename__ = "alunos"

    id = Column(Integer, ForeignKey("pessoas.id"), primary_key=True)
    matricula = Column(Integer, unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "aluno"
    }

    def __str__(self): 
        return f'Aluno | Matrícula: {self.matricula}, {super().__str__()}'

    def fazer_Matricula(self):
        pass

    def cancelar_Matricula(self):
        pass

    def consultar_Treino(self):
        pass