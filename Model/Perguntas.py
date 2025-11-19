class Pergunta:

# Define o construtor padrão da classe Pergunta
    def __init__(self,texto,opcoes):
        self.texto = texto
        self.opcoes = opcoes
        self.resposta = None
#Cria o toString
    def exibir(self):
        print(self.texto)
        for i, opcao in enumerate(self.opcoes,1):
            print(f"{i} - {opcao}")

#Permite armazenar a resposta para as perguntas
    def obterResposta(self):
        while True:
                resposta = int(input(f"Escolha uma opção (1-3): "))
                if 3 >= resposta >= 1:
                    self.resposta = self.opcoes[resposta - 1]
                    break
                else:
                    print("Opção inválida, tente novamente.")
