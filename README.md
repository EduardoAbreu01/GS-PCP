# GS-PCP
  

# Sistema de Orientação de Carreiras e Cursos (Python CLI)

  

Este projeto é um sistema baseado em terminal (CLI) desenvolvido em Python. Seu objetivo é auxiliar usuários na escolha de uma carreira em tecnologia através de um questionário de aptidão, além de listar cursos e trilhas de aprendizado.

  

## Funcionalidades

  

1.  **Realizar Pesquisa:**

* O usuário responde a um questionário técnico e comportamental.

* O sistema utiliza um algoritmo de pontuação (definido em `pesquisa.py`) para calcular a afinidade com as áreas:

*  *Desenvolvedor Back-End*

*  *Desenvolvedor Front-End*

*  *Data Scientist*

*  *Engenheiro DevOps*

*  *Analista de Segurança*

* Ao final, exibe a carreira vencedora e sugere a visualização dos cursos recomendados.

  

2.  **Consultar Cursos:**

* Lista todos os cursos disponíveis no repositório, exibindo nome, categoria e carga horária.

  

3.  **Consultar Carreiras:**

* Exibe as profissões cadastradas e a lista de cursos necessários para cada uma.

  

## Estrutura de Arquivos e Classes

| Módulo | Conteúdo Principal | Descrição |
| :--- | :--- | :--- |
| `Model` | Classes: `Carreira`, `Curso`, `Pergunta` | Define a estrutura dos dados do sistema. |
| `Repository` | Listas: `listaDeCarreiras`, `listaDeCursos`, `listaDePergunta` | Atua como um "Banco de Dados" estático, inicializando todos os dados. |
| `pesquisa.py` | Funções: `realizaPesquisa()`, `calculaAreaRecomendada()` | Contém a **lógica de negócios** (o algoritmo de pontuação e recomendação). |
| `exibeMenus.py` | Funções: `menuMain()`, `exibeMenuUsuario()` | Contém a interface e o fluxo de navegação do sistema (CLI). |

  

## Como Executar

  

1. Instale o **Python** e uma IDE compatível.

2. Baixe o repositório do programa.

3. Execute o projeto utilizando a classe **`main`** dentro da pasta **`outros`**:
