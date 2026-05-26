from sqlalchemy import Column, Integer, String
from database.connection import Base

class Pessoa(Base):

    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    data = Column(String, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    sexo = Column(String, nullable=False)
    tipo = Column(String, nullable=False)

    __mapper_args__ = {
        "polymorphic_on": tipo,   # usa a coluna "tipo" para diferenciar
        "polymorphic_identity": "pessoa"  # o valor padrão é "pessoa"
    }

    def __str__(self):
        return f'{self.nome}, {self.data}, {self.cpf}, {self.sexo}'
    
