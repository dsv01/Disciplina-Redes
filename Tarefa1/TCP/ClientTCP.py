"""
Arquivo com a implementação do lado do cliente utilizando o protocolo tcp para a  
tarefa 1
"""

#Imports do projeto
import socket

# Define o endereço IP e a porta do servidor
HOST = '127.0.0.1'
PORT = 5000

# Cria um socket TCP
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
tcpSocket.connect((HOST, PORT))

# Loop para enviar mensagens
while True:
    # Obtém a mensagem a ser enviada
    message = input('Digite a mensagem: ')

    # Envia a mensagem para o servidor
    tcpSocket.sendall(message.encode())

    # Espera pela resposta do servidor
    data = tcpSocket.recv(1024)
    print(f'Recebido {data.decode()}')

    # Se a mensagem for "exit", encerra a conexão e sai do loop
    if message == 'exit':
        tcpSocket.close()
        break
