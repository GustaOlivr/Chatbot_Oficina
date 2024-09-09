import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

from chatbot.utils import interagir_com_usuario, limpar_terminal, opcoes
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
    
    elif 'serviços' in palavras_pergunta or 'realizados' in palavras_pergunta or 'serviço' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_SERVICOS_REALIZADOS
    
    elif 'finalização' in palavras_pergunta or 'pronta' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_FINALIZACAO
    
    elif 'mais detalhes' in palavras_pergunta or 'detalhes' in palavras_pergunta or 'detalhes da manutenção' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_DETALHES
    
    elif 'atendente' in palavras_pergunta or 'conversar com atendente' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_ATENDENTE
    
    elif 'catalogo' in palavras_pergunta or 'produto' in palavras_pergunta or 'venda' in palavras_pergunta:
        limpar_terminal()
        return RESPOSTA_CATALOGO
    
    else:
        limpar_terminal()
        return RESPOSTA_NAO_ENTENDI

# Executando o chatbot
interagir_com_usuario(MENSAGEM_INICIAL, MENSAGEM_FINAL, PERGUNTA_PECA_PRODUTO, PROMOCAO_CATALOGO, PERGUNTA_SERVICO_STATUS, PERGUNTA_ALGO_MAIS, opcoes, prever_resposta)
