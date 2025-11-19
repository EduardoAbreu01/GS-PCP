from Repository.CursosRepo import listaDeCursos
from Model.Cursos import Curso


def exibeCursos():
    for curso in listaDeCursos:
        Curso.exibir(curso)
