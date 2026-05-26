from database.connection import engine, Session, Base
from entidades.pessoa import Pessoa
from entidades.aluno import Aluno
from entidades.professor import Professor


Base.metadata.create_all(engine) #criando as tabelas no postgreSQL
print('Tabelas Criadas!')

with Session() as session: #inserindo dados na tabela
    aluno = Aluno (
        nome = "Caio Augusto",
        data = "29-06-2002",
        cpf = "123.456.789-10",
        sexo = "Masculino",
        matricula = 1001
    )

    professor = Professor (
        nome = "Marcela Rodrigues",
        data = "08-11-1995",
        cpf = "332.552.123-98",
        sexo = "Feminino",
        cref = "123456-G/SP"
    )

    session.add(aluno)
    session.add(professor)
    session.commit()
    print("Dados inseridos!")

    pessoas = session.query(Pessoa).all()
    for p in pessoas:
        print(p)