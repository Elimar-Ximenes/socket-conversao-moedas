import socket

HOST = "127.0.0.1"
PORT = 5006

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

print("=== Conversor de Moedas (TCP) ===")

for i in range(1, 4):
    print(f"\nRequisição #{i}")
    valor = input("Digite o valor em reais (ex: 10): ")
    moeda = input("Digite a moeda desejada (ex: USD, EUR): ")
    mensagem = f"{valor};{moeda}"
    cliente.send(mensagem.encode())

    resposta = cliente.recv(1024).decode()
    print("Resposta do servidor:", resposta)

cliente.close()
print("\nConexão encerrada.")