"""
Arquivo com a implementação do lado do servidor utilizando o protocolo udp para a  
tarefa 1
"""

#Imports do projeto
import socket

#Definindo dicionário com as palavras a serem traduzidas
words = {"Cadeira":"Chair","Quadro":"Board","Giz":"Chalk",
         "Professor":"Teacher","Aluno":"Student","Universidade":"University",
         "Refeitorio":"cafeteria","Campus":"Campus","Banheiro":"Bathroom","Edificio":"Building"}

# Define o endereço IP e a porta do servidor 
HOST = '127.0.0.1'
PORT = 5000

# Cria um socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind((HOST, PORT))

print('Servidor rodando...')

# Loop infinito para receber requisições
while True:
    # Recebe a mensagem do cliente e o endereço de origem
    data, address = udpSocket.recvfrom(1024)
    print(f'Recebido {data.decode()} de {address}')

    # Envia a resposta para o cliente
    response = words.get(data.decode())
    if(response == None):
        response = "not found"
    udpSocket.sendto(response.encode(), address)
