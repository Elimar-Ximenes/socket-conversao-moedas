# 💱 Socket Conversor de Moedas (UDP e TCP)

Este projeto implementa **clientes e servidores em UDP e TCP usando Python**, simulando um **conversor de moedas**.  
O cliente envia um valor em reais (R$) e a moeda desejada (ex: USD, EUR), e o servidor retorna o valor convertido com base em uma **cotação randômica** gerada para fins de simulação.

## ⚙️ Funcionalidades
- Comunicação via **UDP** e **TCP**.
- **Três requisições** no cliente para demonstração.
- Retorno formatado com cotação e valor convertido.
- Estrutura modular com pastas separadas (`udp/` e `tcp/`).

## 🚀 Como Executar

### 1️⃣ Clonar o repositório
git clone https://github.com/Elimar-Ximenes/socket-conversao-moedas.git  
cd socket-conversao-moedas  

### 2️⃣ Executar a versão UDP
Em um terminal, iniciar o servidor:  
python udp/servidor_udp.py  

Em outro terminal, executar o cliente:  
python udp/cliente_udp.py  

💡 O cliente UDP realizará **três requisições consecutivas**, enviando valores e moedas informados pelo usuário e exibindo as respostas de conversão do servidor.

### 3️⃣ Executar a versão TCP
Em um terminal, iniciar o servidor:  
python tcp/servidor_tcp.py  

Em outro terminal, executar o cliente:  
python tcp/cliente_tcp.py  

💡 O cliente TCP também realizará **três requisições**, demonstrando o comportamento de conexão, envio, resposta e encerramento da sessão.

## 👤 Autor
**Joel Sousa Silva**  
Branch de desenvolvimento: `joel-teste`  
Adaptação e testes baseados no repositório original de **Elimar Ximenes**.

