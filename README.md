# Socket Conversor de Moedas (UDP e TCP)

Este projeto implementa clientes e servidores em **UDP** e **TCP** usando Python.  
O cliente envia um valor em reais (R$) e a moeda desejada (ex: dólar), e o servidor retorna o valor convertido.  
A cotação da moeda é gerada de forma randômica para simulação.

---

## 🚀 Como executar

### 1. Clonar o repositório
`git clone https://github.com/seu-usuario/socket-conversao-moedas.git`

`cd socket-conversao-moedas`

### 2. Executar a versão UDP

- Em um terminal, iniciar o servidor:
  
`python udp/servidor_udp.py`

- Em outro terminal, executar o cliente:

`python udp/cliente_udp.py`

### 2. Executar a versão TCP

- Em um terminal, iniciar o servidor:
  
`python udp/servidor_tcp.py`

- Em outro terminal, executar o cliente:

`python udp/cliente_tcp.py`
