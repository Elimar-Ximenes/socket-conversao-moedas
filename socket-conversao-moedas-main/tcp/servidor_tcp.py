import socket
import random

def obter_cotacao(moeda):
    return round(random.uniform(4.5, 6.0), 2)

HOST = "127.0.0.1"
PORT = 5006

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("Servidor TCP aguardando conexões...")

conn, addr = server.accept()
print("Conectado em:", addr)

try:
    for i in range(3):  # processa 3 requisições na MESMA conexão
        dados = conn.recv(1024)
        if not dados:
            break
        valor_str, moeda = dados.decode().strip().split(";")
        valor = float(valor_str)

        cotacao = round(random.uniform(4.5, 6.0), 2)
        convertido = round(valor / cotacao, 2)
        resposta = f"Cotação usada: {cotacao} | {valor} BRL = {convertido} {moeda.upper()}"
        conn.send(resposta.encode())
finally:
    conn.close()
    server.close()