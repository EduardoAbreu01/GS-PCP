from Model.Perguntas import *


#Cria as perguntas Comportamentais
pergunta1 = Pergunta(
    "Como você aborda um problema lógico complexo?",
    ["Divido em etapas menores", "Tento resolver tudo de uma vez", "Tenho dificuldade em começar"]
)

pergunta2 = Pergunta(
    "Você costuma propor soluções inovadoras para problemas antigos?",
    ["Sim, frequentemente", "Às vezes, se solicitado", "Prefiro seguir o padrão estabelecido"]
)

pergunta3 = Pergunta(
    "Como você se sente trabalhando em equipe?",
    ["Produzo melhor em grupo", "Gosto, mas prefiro trabalhar só", "Sinto que meu rendimento cai"]
)

pergunta4 = Pergunta(
    "Como você reage quando o escopo do projeto muda repentinamente?",
    ["Adapto-me rapidamente", "Fico frustrado, mas aceito", "Tenho muita dificuldade em mudar"]
)

pergunta5 = Pergunta(
    "Você consegue priorizar tarefas e cumprir prazos apertados?",
    ["Sim, com facilidade", "Mais ou menos, às vezes atraso", "Não, perco-me na organização"]
)

pergunta6 = Pergunta(
    "Como é o seu desempenho em situações de alta pressão?",
    ["Mantenho a calma e o foco", "Fico ansioso, mas entrego", "Paraliso e não consigo produzir"]
)

pergunta7 = Pergunta(
    "Diante de um impasse na equipe, qual a sua atitude?",
    ["Tomo a iniciativa para resolver", "Espero alguém decidir", "Evito me envolver"]
)

pergunta8 = Pergunta(
    "Como você lida com divergências de opinião com um colega?",
    ["Busco o diálogo e consenso", "Ignoro para evitar atrito", "Imponho minha visão"]
)

pergunta9 = Pergunta(
    "Com que frequência você estuda novas tecnologias ou metodologias?",
    ["Constantemente/Diariamente", "Apenas quando o trabalho exige", "Raramente"]
)

pergunta10 = Pergunta(
    "Como você recebe críticas construtivas sobre seu trabalho?",
    ["Vejo como oportunidade de evoluir", "Fico chateado momentaneamente", "Levo para o lado pessoal"]
)

#Cria as perguntas de Hard Skills
pergunta11 = Pergunta("Qual o seu nível em Java?",
    ["Iniciante", "Intermediário", "Avançado"])

pergunta12 = Pergunta("Qual o seu nível em Python?",
    ["Iniciante", "Intermediário", "Avançado"])

pergunta13 = Pergunta("Domínio de SQL?",
    ["Básico (Selects simples)", "Intermediário (Joins/Group By)", "Avançado (Procedures/Otimização)"])

pergunta14 = Pergunta("Conhecimento em Git?",
    ["Apenas commit/push", "Gerenciamento de branches/merge", "Fluxos complexos/Rebase"])

pergunta15 = Pergunta("Experiência com Docker?",
    ["Nunca utilizei", "Sei rodar containers", "Cro Dockerfiles e Composes"])

pergunta16 = Pergunta("Uso de Frameworks Backend?",
    ["Nenhum", "Sei o básico", "Domínio completo da arquitetura"])

pergunta17 = Pergunta("Nível em Frontend?",
    ["Básico", "Consigo criar layouts responsivos", "Avançado (React/Angular/Vue)"])

pergunta18 = Pergunta("Conhecimento em Cloud?",
    ["Nenhum", "Implantação simples", "Arquitetura e serviços gerenciados"])

pergunta19 = Pergunta("Conforto com terminal Linux?",
    ["Prefiro interface gráfica", "Sei comandos básicos", "Automatizo tarefas via Shell Script"])

pergunta20 = Pergunta("Nível de Inglês para leitura?",
    ["Uso tradutor constantemente", "Leio com ajuda ocasional", "Leio documentação fluentemente"])


#Inicializa uma lista e armazena todas as perguntas
listaDePergunta = [
    pergunta1, pergunta2, pergunta3, pergunta4, pergunta5,
    pergunta6, pergunta7, pergunta8, pergunta9, pergunta10,
    pergunta11, pergunta12, pergunta13, pergunta14, pergunta15,
    pergunta16, pergunta17, pergunta18, pergunta19, pergunta20
]