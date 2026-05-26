from entidades.pessoa import Pessoa
from database.connection import Base
from sqlalchemy import Column, Integer, ForeignKey, String

class Professor(Pessoa): #subclasse Professor

    __tablename__ = "professores"

    id = Column(Integer, ForeignKey('pessoas.id'), primary_key=True)
    cref = Column(String, unique=True, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "professor"
    }

    def __str__(self):
        return f'Professor | CREF: {self.cref}, {super().__str__()}'
    
    def consultar_Aluno(self):
        pass

    def criar_Treino(self):
        pass