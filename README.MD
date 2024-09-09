# Chatbot de Atendimento para Oficina de Motocicletas

Este projeto é um **chatbot de atendimento** desenvolvido para uma oficina de motocicletas, que simula um sistema de árvore de decisão e utiliza técnicas de **Processamento de Linguagem Natural (NLP)** para gerar respostas dinâmicas. O chatbot foi projetado para auxiliar clientes em questões relacionadas a serviços de manutenção, troca de peças, e informações sobre o status de suas motocicletas.

## Contexto

O chatbot foi criado para automatizar o atendimento de uma oficina especializada em motocicletas, oferecendo suporte ao cliente em várias situações, como:

-   **Status de Manutenção**: Informações sobre o andamento dos serviços realizados nas motocicletas.
-   **Catálogo de Peças e Produtos**: Exibição de itens disponíveis para venda, como óleos e freios.
-   **Serviços Realizados**: Detalhes sobre as manutenções realizadas, incluindo troca de peças e ajustes.
-   **Atendimento Personalizado**: Possibilidade de encaminhar o cliente para um atendente humano especializado quando necessário.

O projeto simula a árvore de decisão para determinar a resposta com base nas perguntas do usuário, e também utiliza técnicas de NLP para entender a intenção do cliente e gerar respostas apropriadas.

## Tecnologias Utilizadas

-   **Python 3.x**
-   **Técnicas de NLP** para processamento de linguagem e tomada de decisão.
-   Estrutura de **árvore de decisão** para respostas predefinidas.

## Funcionalidades

1.  **Respostas Pré-Definidas**: O chatbot oferece uma série de respostas automáticas baseadas em perguntas específicas.
2.  **Tomada de Decisão com NLP**: Usa técnicas básicas de NLP para interpretar e responder de forma dinâmica.
3.  **Manutenção e Serviços**: Fornece informações sobre o status da manutenção da motocicleta e detalhes dos serviços realizados.
4.  **Venda de Produtos**: Exibe o catálogo de peças e produtos disponíveis.
5.  **Escalonamento para Atendente**: Informa ao usuário quando um atendente especializado entrará em contato para suporte adicional.

## Como Rodar o Projeto

### Pré-Requisitos

-   **Python 3.x** instalado na máquina.
-   NLTK (Natural Language Toolkit) para processamento de linguagem natural.
*OBS*: Dependências básicas listadas em `requirements.txt`.

### Instalação

1.  Clone o repositório em sua máquina local:

`git clone https://github.com/seu-usuario/chatbot-oficina.git` 

2.  Acesse o diretório do projeto:

`cd chatbot-oficina` 

3.  (Opcional) Crie um ambiente virtual:

`python -m venv venv`
`source venv/bin/activate  # Linux/Mac`
`venv\Scripts\activate  # Windows` 

4.  Instale as dependências (se houver um `requirements.txt`):

`pip install -r requirements.txt` 

### Executando o Chatbot

Para iniciar o chatbot, basta rodar o arquivo `main.py`:

`python main.py` 

Ao executar o comando, o chatbot abrirá um prompt no terminal para interação. Basta seguir as instruções fornecidas para obter informações sobre serviços, status da motocicleta ou catálogo de produtos.

*OBS*: lembre-se de estar na pasta do chatbot

## Exemplo de Uso

`Chatbot: Olá! Estou aqui para ajudar com sua motocicleta. Sobre o que você gostaria de saber?`
`Usuário: Qual o status da manutenção?`
`Chatbot: A manutenção da sua moto está em progresso e tem previsão de ser finalizada até as 10 horas do próximo dia.` 

## Contribuições

Fique à vontade para abrir **issues** e **pull requests** se você deseja contribuir com o projeto.