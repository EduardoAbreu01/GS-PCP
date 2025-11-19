from Model.Carreiras import *
from Repository.CursosRepo import *

#Cria as carreiras
carreira1 = Carreira("Desenvolvedor Back-End","Programação")
carreira2 = Carreira("Desenvolvedor Front-End","Programação")
carreira3 = Carreira("Data Scientist", "Data Science")
carreira4 = Carreira("Engenheiro DevOps", "Cloud e DevOps")
carreira5 = Carreira("Analista de Segurança", "CyberSecurity")


#Adiciona Cursos as suas respectivas carreiras
carreira1.adicionarCursos([curso1,curso4,curso5,curso6,curso15,curso10])
carreira2.adicionarCursos([curso3,curso10,curso13,curso15])
carreira3.adicionarCursos([curso2,curso4,curso11,curso10,curso14,curso12])
carreira4.adicionarCursos([curso6,curso15,curso9,curso7,curso12])
carreira5.adicionarCursos([curso9, curso7, curso6, curso2, curso10,curso12])


#Inicializa uma lista e adiciona as carreiras nela
listaDeCarreiras = [carreira1,carreira2,carreira3,carreira4,carreira5]