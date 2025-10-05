import socket
import random

def obter_cotacao(moeda):
    # Gera uma cotação aleatória entre 4.5 e 6.0 para dólar, euro etc.
    return round(random.uniform(4.5, 6.0), 2)

HOST = "127.0.0.1"
PORT = 5006
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("Servidor TCP aguardando conexões...")

while True:
    conn, addr = server.accept()
    print("Conectado em:", addr)
    dados = conn.recv(1024).decode()

    valor, moeda = dados.split(";")
    valor = float(valor)

    cotacao = obter_cotacao(moeda)
    convertido = round(valor / cotacao, 2)

    resposta = f"Cotação usada: {cotacao} | {valor} BRL = {convertido} {moeda.upper()}"
    conn.send(resposta.encode())
    conn.close()