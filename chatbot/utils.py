import os

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

# Função para pular linha no output
def pular_linhas(num_linhas=1):
    """Imprime um número específico de linhas em branco."""
    print('\n' * num_linhas)

# Lista de opções
opcoes = [
    "1. Verificar status da manutenção",
    "2. Consultar serviços realizados",
    "3. Consultar catalogo de venda de produtos e peças",
    "4. Ver mais detalhes",
    "5. Falar com um atendente",
    "6. Sair"
]

# Função para exibir opções
def exibir_opcoes(opcoes):
    print("Escolha uma das opções abaixo:")
    pular_linhas(1)
    for opcao in opcoes:
        print(opcao)

# Função para limpar o terminal
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para interação com o usuário
def interagir_com_usuario(MENSAGEM_INICIAL, MENSAGEM_FINAL, PERGUNTA_PECA_PRODUTO, PROMOCAO_CATALOGO, PERGUNTA_SERVICO_STATUS, PERGUNTA_ALGO_MAIS, opcoes, prever_resposta):
    limpar_terminal()
    print(MENSAGEM_INICIAL)
    pular_linhas(1)
    exibir_opcoes(opcoes)

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
            exibir_opcoes(opcoes)
            
        elif 'catalogo' in pergunta:
            exibir_catalogo()
            print(PROMOCAO_CATALOGO)
            pular_linhas(1)
            exibir_opcoes(opcoes)
            
        elif 'serviço' in pergunta or 'status' in pergunta:
            pular_linhas(1)
            print(PERGUNTA_SERVICO_STATUS)
            exibir_opcoes(opcoes)
            
        elif "Desculpe, não entendi sua pergunta" in resposta:
            pular_linhas(1)
            
        else:
            pular_linhas(1)
            print(PERGUNTA_ALGO_MAIS)
            exibir_opcoes(opcoes)
