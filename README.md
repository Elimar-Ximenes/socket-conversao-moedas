# Socket Conversor de Moedas (UDP e TCP)

Este projeto implementa clientes e servidores em **UDP** e **TCP** usando Python.  
O cliente envia um valor em reais (R$) e a moeda desejada (ex: dólar), e o servidor retorna o valor convertido.  
A cotação da moeda é gerada de forma randômica para simulação.

> Esta branch foi desenvolvida com foco na questão 8. O código referente à questão 9 pode ser encontrado na branch *joel-teste*. De forma geral, ambos os códigos são praticamente iguais, diferindo apenas em alguns ajustes nos *prints* e na adaptação que permite ao usuário realizar as três requisições de conversão em sequência, conforme solicitado na questão.
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

### 3. Executar a versão TCP

- Em um terminal, iniciar o servidor:
  
`python tcp/servidor_tcp.py`

- Em outro terminal, executar o cliente:

`python tcp/cliente_tcp.py`
