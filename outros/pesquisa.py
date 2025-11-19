from Model.Carreiras import *
from Model.Perguntas import *
from Repository.CarreirasRepo import listaDeCarreiras

from exibeMenus import *


from Repository.PerguntasRepo import listaDePergunta

#Cria a função que Recomenda uma área baseado nas respostas do usuário
def calculaAreaRecomendada():

#Cria o dicionário que irá armazenar os pontos do questionário
    pontos = {
        "Desenvolvedor Back-End": 0,
        "Desenvolvedor Front-End": 0,
        "Data Scientist": 0,
        "Engenheiro DevOps": 0,
        "Analista de Segurança": 0
    }

#Realiza as perguntas e contabiliza os pontos de acordo com a resposta do usuário
    pergunta11 = listaDePergunta[10].resposta
    if pergunta11 == "Avançado":
        pontos["Desenvolvedor Back-End"] += 3
        pontos["Engenheiro DevOps"] += 2
        pontos["Desenvolvedor Front-End"] += 1
    elif pergunta11 == "Intermediário":
        pontos["Desenvolvedor Back-End"] += 2
        pontos["Engenheiro DevOps"] += 1

    pergunta12 = listaDePergunta[11].resposta
    if pergunta12 == "Avançado":
        pontos["Data Scientist"] += 3
        pontos["Analista de Segurança"] += 2
        pontos["Desenvolvedor Back-End"] += 1
    elif pergunta12 == "Intermediário":
        pontos["Data Scientist"] += 2
        pontos["Desenvolvedor Back-End"] += 1

    pergunta13 = listaDePergunta[12].resposta
    if "Avançado" in pergunta13:
        pontos["Data Scientist"] += 3
        pontos["Desenvolvedor Back-End"] += 3
    elif "Intermediário" in pergunta13:
        pontos["Data Scientist"] += 2
        pontos["Desenvolvedor Back-End"] += 1

    pergunta14 = listaDePergunta[13].resposta
    if "Fluxos complexos" in pergunta14:
        pontos["Engenheiro DevOps"] += 3
        pontos["Desenvolvedor Back-End"] += 1
        pontos["Desenvolvedor Front-End"] += 1
    elif "Gerenciamento" in pergunta14:
        pontos["Engenheiro DevOps"] += 1

    pergunta15 = listaDePergunta[14].resposta
    if "Crio Dockerfiles" in pergunta15:
        pontos["Engenheiro DevOps"] += 3
        pontos["Desenvolvedor Back-End"] += 2
    elif "Sei rodar" in pergunta15:
        pontos["Engenheiro DevOps"] += 1

    pergunta16 = listaDePergunta[15].resposta
    if "Domínio completo" in pergunta16:
        pontos["Desenvolvedor Back-End"] += 3
    elif "Sei o básico" in pergunta16:
        pontos["Desenvolvedor Back-End"] += 1

    pergunta17 = listaDePergunta[16].resposta
    if "Avançado" in pergunta17:
        pontos["Desenvolvedor Front-End"] += 3
    elif "Consigo criar" in pergunta17:
        pontos["Desenvolvedor Front-End"] += 2

    pergunta18 = listaDePergunta[17].resposta
    if "Arquitetura" in pergunta18:
        pontos["Engenheiro DevOps"] += 3
        pontos["Analista de Segurança"] += 2
        pontos["Desenvolvedor Back-End"] += 1
    elif "Implantação simples" in pergunta18:
        pontos["Engenheiro DevOps"] += 1

    pergunta19 = listaDePergunta[18].resposta
    if "Automatizo" in pergunta19:
        pontos["Engenheiro DevOps"] += 3
        pontos["Analista de Segurança"] += 3
    elif "Sei comandos básicos" in pergunta19:
        pontos["Engenheiro DevOps"] += 1
        pontos["Analista de Segurança"] += 1

#Acessa o dicionário "pontos" e retorna a área com a maior quantidade de pontos
    carreiraRecomendada = max(pontos, key=pontos.get)
    print(f"Resultado: {carreiraRecomendada} com {pontos[carreiraRecomendada]} pontos.")
    print(f"""Deseja receber recomendações de cursos para a área de {carreiraRecomendada}?"
    1- Sim
    2- Não
    """)
    resposta = int(input())
#Caso o usuário responda 1 para a pergunta o sistema recomenda cursos da carreira recomendada
    if resposta == 1:
        for carreira in listaDeCarreiras:
            if carreira.nome == carreiraRecomendada:
                Carreira.exibir(carreira)
    else:
        quit()






def realizaPesquisa():
    i = 1
    print("**********************************************")
    for perguntas in listaDePergunta:
        print(f"\nQuestão - {i}\n")
        Pergunta.exibir(perguntas)
        Pergunta.obterResposta(perguntas)
        i += 1
        print("\n**********************************************")
    print("Analisando o seu perfil.....")
    print("Obtendo a resposta...")
    calculaAreaRecomendada()


