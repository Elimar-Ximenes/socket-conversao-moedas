import socket

HOST = "127.0.0.1"
PORT = 5005
cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("=== Conversor de Moedas (UDP) ===")

for i in range(1, 4):
    print(f"\nRequisição #{i}")
    valor = input("Digite o valor em reais (ex: 10): ")
    moeda = input("Digite a moeda desejada (ex: USD, EUR): ")

    mensagem = f"{valor};{moeda}"
    cliente.sendto(mensagem.encode(), (HOST, PORT))

    resposta, _ = cliente.recvfrom(1024)
    print("Resposta do servidor:", resposta.decode())

cliente.close()
print("\nTodas as requisições foram concluídas com sucesso.")