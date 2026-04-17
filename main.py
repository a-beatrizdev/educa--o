from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    materia = Column(String(100), nullable=False)
    salario = Column(Integer, nullable=False)

    aulas = relationship("Aula", back_populates="professores")

    def __repr__(self):
        return f"Professor: id={self.id} - nome={self.nome} - materia={self.materia} - salario={self.salario}"

class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    duracao = Column(Integer, nullable=False)
    alunos_presentes = Column(Float, nullable=False)

    professores_id = Column(Integer, ForeignKey("professores.id"))
    professores = relationship("Professor", back_populates="aulas")

    def __repr__(self):
        return f"id={self.id} - nome={self.nome} - duracao={self.duracao} - alunos_presentes={self.alunos_presentes}"

engine = create_engine("sqlite:///educacao.db")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def cadastrar_professor():
    with Session() as session:
        try:
            nome_professor = input("Digite o nome do professor: ").capitalize()
            materia = input("Digite a matéria do professor: ").capitalize()
            salario = input("Digite o salário do professor: ").capitalize()
            professor = Professor(nome=nome_professor, materia=materia, salario=salario)

            session.add(professor)
            session.commit()
            print(f"Professor cadastrado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

# cadastrar_professor()
        
def cadastrar_aula():
    with Session() as session:
        try:
            nome_professor = input("Digite o nome do professor: ").capitalize()
            professor = session.query(Professor).filter_by(nome=nome_professor).first()
            if professor == None:
                print(f"Nenhum professor encontrado com esse nome {nome_professor}!")
                return
            else: 
                nome = input("Digite o nome da aula: ").capitalize()
                duracao = input("Digite o tempo de duração da aula: ").capitalize()
                alunos_presentes = input("Digite a quantidade de alunos presentes: ").capitalize()
                aulas = Aula(nome=nome, duracao=duracao, alunos_presentes=alunos_presentes, professores=professor)
                # aula.professores.append(professor)
                session.add(aulas)
                session.commit()
            print(f"Aula cadastrada com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

cadastrar_aula()