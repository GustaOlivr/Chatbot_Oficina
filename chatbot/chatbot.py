import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer

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

def prever_resposta(pergunta):
    palavras_pergunta = processar_texto(pergunta)
    
    # Simulação de árvore de decisão com if-else
    if 'status' in palavras_pergunta or 'manutenção' in palavras_pergunta:
        return "A manutenção da sua moto está em progresso e tem previsão de ser finalizada até as 10 horas do próximo dia."
    
    elif 'serviço' in palavras_pergunta or  'realizados' in palavras_pergunta or 'serviços' in palavras_pergunta:
        return """Os serviços solicitados incluem:
        * Troca de óleo - cód: 1548;
        * Troca do filtro de óleo - cód: 6523;
        * Troca dos freios dianteiros - cód: 5487;"""
    
    elif 'finalização' in palavras_pergunta or 'pronta' in palavras_pergunta:
        return "O serviço tem previsão de ser concluído até as 10 horas de amanhã."
    
    elif 'peças' in palavras_pergunta or 'produto' in palavras_pergunta:
        return "Vendemos peças para motocicletas, capacetes e outros produtos relacionados. Precisa de algo específico?"
    
    elif 'mais detalhes' in palavras_pergunta or 'detalhes' in palavras_pergunta:
        return """ Detalhes do serviço:
* Troca de óleo - Yamalube 20w-50
* Troca do filtro de óleo - Filtro De Oleo Fazer Lander Tenere 250 X-max Original Yamaha
* Troca dos freios dianteiros - Disco Freio Dianteiro Fazer 250 Fz 15 2018 Até 2024 - MTBR"""
    
    else:
        return "Desculpe, não entendi sua pergunta. Poderia reformular?"
