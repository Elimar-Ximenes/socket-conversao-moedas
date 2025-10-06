import socket
import random

def obter_cotacao(moeda):
    # Gera uma cotação aleatória entre 4.5 e 6.0 para dólar, euro etc.
    return round(random.uniform(4.5, 6.0), 2)

# Configura o servidor
HOST = "127.0.0.1"
PORT = 5005
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Servidor UDP aguardando mensagens...")

while True:
    dados, endereco = server.recvfrom(1024)
    mensagem = dados.decode()
    valor, moeda = mensagem.split(";")
    valor = float(valor)

    cotacao = obter_cotacao(moeda)
    convertido = round(valor / cotacao, 2)

    resposta = f"Cotação usada: {cotacao} | {valor} BRL = {convertido} {moeda.upper()}"
    server.sendto(resposta.encode(), endereco)
