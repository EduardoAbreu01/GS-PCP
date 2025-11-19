from fileinput import close

from pesquisa import realizaPesquisa
from exibeCursos import exibeCursos
from exibeCarreiras import exibeCarreiras

#Cria a função que exibe o menu para interagir com o usuário

def exibeMenuUsuario():
    print("""******MENU*******
1- Realizar Pesquisa
2- Consultar Cursos
3- Consultar Carreiras
0- Sair""")
    leitura = int((input("Digite: ")))
    if leitura == 1:
        realizaPesquisa()
    if leitura == 2:
        exibeCursos()
    if leitura == 3:
        exibeCarreiras()
    if leitura == 0:
        quit()
    return leitura



def menuMain():
    exibeMenuUsuario()