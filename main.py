import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import os


# Baixando os recursos necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('rslp')

# Texto de conhecimento do chatbot (informações sobre o cliente e serviço)
texto_base = """
Cliente deixou a motocicleta Fazer 250 Yamaha, ano 2017, para a realização dos seguintes serviços: 
troca de óleo, troca do filtro de óleo e troca dos freios dianteiros. A manutenção está atualmente com 
o status de 'Em progresso' e tem previsão de ser finalizada até as 10 horas do próximo dia.
"""

# PNL - Processamento de texto: Tokenização e remoção de stopwords
def processar_texto(texto):
    palavras = word_tokenize(texto.lower())
    stop_words = set(stopwords.words('portuguese'))
    palavras_filtradas = [palavra for palavra in palavras if palavra.isalnum() and palavra not in stop_words]
    
    return palavras_filtradas

# Processar o texto base
palavras_processadas_base = processar_texto(texto_base)

# Função para prever a resposta do chatbot usando if-else
def prever_resposta(pergunta):
    palavras_pergunta = processar_texto(pergunta)
    
    # Simulação de árvore de decisão com if-else
    if 'status' in palavras_pergunta or 'manutenção' in palavras_pergunta:
        limpar_terminal()
        return "A manutenção da sua moto está em progresso e tem previsão de ser finalizada até as 10 horas do próximo dia."
    
    elif 'serviço' in palavras_pergunta or 'realizados' in palavras_pergunta:
        limpar_terminal()
        return """Os serviços solicitados incluem:
        * Troca de óleo - cód: 1548;
        * Troca do filtro de óleo - cód: 6523;
        * Troca dos freios dianteiros - cód: 5487;"""
    
    elif 'finalização' in palavras_pergunta or 'pronta' in palavras_pergunta:
        limpar_terminal()
        return "O serviço tem previsão de ser concluído até as 10 horas de amanhã."
    
    elif 'peça' in palavras_pergunta or 'produto' in palavras_pergunta or 'catalogo' in palavras_pergunta:
        limpar_terminal()
        return "Vendemos peças para motocicletas, capacetes e outros produtos relacionados."
    
    elif 'mais detalhes' in palavras_pergunta or 'detalhes' in palavras_pergunta:
        limpar_terminal()
        return """ Detalhes do serviço:
        * Troca de óleo - Yamalube 20w-50
        * Troca do filtro de óleo - Filtro De Oleo Fazer Lander Tenere 250 X-max Original Yamaha
        * Troca dos freios dianteiros - Disco Freio Dianteiro Fazer 250 Fz 15 2018 Até 2024 - MTBR"""
    
    elif 'atendente' in palavras_pergunta or 'conversar com atendente' in palavras_pergunta:
        limpar_terminal()
        return "O atendente especializado entrará em contato com você para melhor atende-lo"
    
    else:
        limpar_terminal()
        return "Desculpe, não entendi sua pergunta. Poderia reformular?"

# Lista de opções
opcoes = [
    "1. Verificar status da manutenção",
    "2. Consultar serviços realizados",
    "3. Consultar catalogo de venda de produtos e peças",
    "4. Falar com um atendente",
    "5. Sair"
]

# Pular linha no output
def pular_linhas(num_linhas=1):
    """Imprime um número específico de linhas em branco."""
    print('\n' * num_linhas)

# Função para exibir opções
def exibir_opcoes():
    print("Escolha uma das opções abaixo:")
    pular_linhas(1)
    for opcao in opcoes:
        print(opcao)

def limpar_terminal():
    os.system('cls')

    
# Função para interação com o usuário (fazendo perguntas)
def interagir_com_usuario():
    limpar_terminal()
    print("Chatbot: Olá! Estou aqui para ajudar com sua motocicleta. Sobre o que você gostaria de saber?")
    pular_linhas(1)
    exibir_opcoes()

    while True:
        pular_linhas(1)
        pergunta = input("Você: ")
        
        if pergunta.lower() == "sair":
            print("Chatbot: Obrigado por usar o serviço. Até logo!")
            break
        
        resposta = prever_resposta(pergunta)
        print(f"Chatbot: {resposta}")
        
        # Fazer perguntas ao cliente com base no fluxo da conversa
        if 'peças' in pergunta or 'produto' in pergunta:
            print("""Chatbot: Gostaria de saber mais sobre as peças ou produtos que vendemos? 
* Se sim, responda com 'consultar catalogo'
* Se não, digite 'sair' """)
        elif 'serviço' in pergunta or 'status' in pergunta:
            pular_linhas(1)
            print("""Chatbot: Deseja mais detalhes sobre os serviços que foram realizados? 
* Se sim responda com 'mais detalhes' 
* Se não, digite 'sair'.""")
        elif "Desculpe, não entendi sua pergunta" in resposta:
            pular_linhas(1)
        else:
            pular_linhas(2) 
            print("Chatbot: Há mais alguma coisa sobre a qual você gostaria de saber?")
            exibir_opcoes()

# Executando o chatbot
interagir_com_usuario()
