import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
import os

from respotas_chatbot import RESPOSTA_ATENDENTE, RESPOSTA_CATALOGO, RESPOSTA_DETALHES, RESPOSTA_FINALIZACAO, RESPOSTA_NAO_ENTENDI, RESPOSTA_SERVICOS_REALIZADOS, RESPOSTA_STATUS, MENSAGEM_INICIAL, PERGUNTA_PECA_PRODUTO,PERGUNTA_SERVICO_STATUS,PROMOCAO_CATALOGO,PERGUNTA_ALGO_MAIS,MENSAGEM_FINAL


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
    
    if 'status' in palavras_pergunta or 'manutenção' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_STATUS
    
    elif 'serviço' in palavras_pergunta or 'realizados' in palavras_pergunta or 'serviços   ' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_SERVICOS_REALIZADOS
    
    elif 'finalização' in palavras_pergunta or 'pronta' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_FINALIZACAO
    
    elif 'mais detalhes' in palavras_pergunta or 'detalhes' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_DETALHES
    
    elif 'atendente' in palavras_pergunta or 'conversar com atendente' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_ATENDENTE
    
    elif 'catalogo' in palavras_pergunta or 'produto' in palavras_pergunta or 'venda' in palavras_pergunta or 'produtos' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_CATALOGO
    
    else:
        limpar_terminal()
        return RESPOSTA_NAO_ENTENDI
# Lista de opções
opcoes = [
    "1. Verificar status da manutenção",
    "2. Consultar serviços realizados",
    "3. Consultar catalogo de venda de produtos e peças",
    "4. Ver detalhes da manutenção",
    "5. Falar com um atendente",
    "6. Sair"
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
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o catálogo de produtos
def exibir_catalogo():
    catalogo = [
        "1. Capacete X-Rider - R$ 299,00",
        "2. Luvas de Motociclista - R$ 149,00",
        "3. Jaqueta de Couro - R$ 499,00",
        "4. Botas de Motociclista - R$ 349,00",
        "5. Óleo Sintético 10w-40 - R$ 89,00",
        "6. Filtro de Ar Yamaha - R$ 59,00",
        "7. Disco de Freio Dianteiro - R$ 149,00",
        "8. Pastilhas de Freio Dianteiras - R$ 89,00",
        "9. Espelho Retrovisor - R$ 75,00",
        "10. Amortecedor Traseiro - R$ 399,00",
        "11. Guidão Ajustável - R$ 120,00",
        "12. Manoplas de Acelerador - R$ 40,00",
        "13. Lanterna Traseira LED - R$ 95,00",
        "14. Farol Halógeno - R$ 150,00",
        "15. Bateria 12V - R$ 180,00",
        "16. Capa de Moto - R$ 75,00",
        "17. Suporte para GPS - R$ 60,00",
        "18. Sistema de Alarme - R$ 220,00",
        "19. Protetor de Motor - R$ 130,00",
        "20. Kit de Ferramentas - R$ 110,00"
    ]
    print("Catálogo de Produtos e Peças:")
    pular_linhas(1)
    for item in catalogo:
        print(item)
    pular_linhas(1)

# Função para interação com o usuário (fazendo perguntas)
def interagir_com_usuario():
    limpar_terminal()
    print(MENSAGEM_INICIAL)
    pular_linhas(1)
    exibir_opcoes()

    while True:
        pular_linhas(1)
        pergunta = input("Você: ")
        
        if pergunta.lower() == "sair":
            print(MENSAGEM_FINAL)
            break
        
        resposta = prever_resposta(pergunta)
        print(f"Chatbot: {resposta}")
        
        if 'peças' in pergunta or 'produto' in pergunta:
            pular_linhas(1)
            print(PERGUNTA_PECA_PRODUTO)
            exibir_opcoes()
            
        elif 'catalogo' in pergunta:
            exibir_catalogo()
            print(PROMOCAO_CATALOGO)
            pular_linhas(1)
            exibir_opcoes()
            
        elif 'serviço' in pergunta or 'status' in pergunta:
            pular_linhas(1)
            print(PERGUNTA_SERVICO_STATUS)
            exibir_opcoes()
            
        elif "Desculpe, não entendi sua pergunta" in resposta:
            pular_linhas(1)
            
        else:
            pular_linhas(2)
            print(PERGUNTA_ALGO_MAIS)
            exibir_opcoes()

# Executando o chatbot
interagir_com_usuario()