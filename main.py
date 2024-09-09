from chatbot.chatbot import processar_texto, prever_resposta

# Lista de opções
opcoes = [
    "1. Verificar status da manutenção",
    "2. Consultar serviços realizados",
    "3. Obter detalhes sobre peças e produtos",
    "4. Falar com um atendente",
    "5. Sair"
]

def pular_linhas(num_linhas=1):
    """Imprime um número específico de linhas em branco."""
    print('\n' * num_linhas)

def exibir_opcoes():
    print("Escolha uma das opções abaixo:")
    for opcao in opcoes:
        print(opcao)

def interagir_com_usuario():
    print("Chatbot: Olá! Estou aqui para ajudar com sua motocicleta. Sobre o que você gostaria de saber?")
    exibir_opcoes()

    while True:
        pergunta = input("Você: ")
        
        if pergunta.lower() == "sair":
            print("Chatbot: Obrigado por usar o serviço. Até logo!")
            break
        
        resposta = prever_resposta(pergunta)
        print(f"Chatbot: {resposta}")
        
        # Fazer perguntas ao cliente com base no fluxo da conversa
        if 'peças' in pergunta or 'produto' in pergunta:
            print("Chatbot: Gostaria de saber mais sobre as peças ou produtos que vendemos?")
        elif 'serviço' in pergunta or 'status' in pergunta:
            print("Chatbot: Deseja mais detalhes sobre os serviços que foram realizados? Se sim responda com 'mais detalhes', se não, digite 'sair'.")
        else:
            pular_linhas(2)
            print("Chatbot: Há mais alguma coisa sobre a qual você gostaria de saber?")
            exibir_opcoes()
            pular_linhas(2)

# Executando o chatbot
interagir_com_usuario()
