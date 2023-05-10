"""
Arquivo com a implementação do lado do cliente utilizando o protocolo udp para a  
tarefa 1
"""

#Imports do projeto
import socket

# Define o endereço IP e a porta do servidor
HOST = '127.0.0.1'
PORT = 5000

# Cria um socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Loop para enviar requisições
while True:
    # Obtém a mensagem a ser enviada
    message = input('Digite uma palavra: ')

    # Envia a mensagem para o servidor
    udpSocket.sendto(message.encode(), (HOST, PORT))

    # Espera pela resposta do servidor
    data, address = udpSocket.recvfrom(1024)
    print(f'Em Ingles: {data.decode()}  {address}')
