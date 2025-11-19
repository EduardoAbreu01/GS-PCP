from Model.Cursos import Curso

class Carreira:
#Define o construtor padrão da classe Carreira
    def __init__(self,nome,area):
        self.nome = nome
        self.area = area
#Inicializa uma lista vazia para armazenar os objetos da classe Curso
        self.cursos = []
#Cria o toString
    def exibir(self):
        print("\nProfissão: " + self.nome + " Área: " + self.area + " Cursos Recomendados: ")
#Acessa os atributos do objeto curso (nome e carga) e imprime
        for cursos in self.cursos:
            print(cursos.nome + " " + cursos.carga)

#Permite adicionar cursos a carreira
    def adicionarCursos(self,curso):
        if isinstance(curso, list):
            self.cursos.extend(curso)
        else:
            self.cursos.append(curso)





