from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    materia = Column(String(100), nullable=False)
    salario = Column(Integer, nullable=False)

    aulas = relationship("Aula", back_populates="professor")

    def __init__(self, nome):
        self.nome = nome

        def __repr__(self):
            return f"Professor: id={self.id} - nome={self.nome}"

class Aula(Professor):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    duracao = Column(Integer, nullable=False)
    alunos_presentes = Column(Integer, nullable=False)

    professor = Column(Integer, ForeignKey ("professores.id"))

    def __repr__(self):
        return f"id={self.id} - nome={self.nome}"

