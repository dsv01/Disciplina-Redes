"""
Arquivo com a implementação do lado do servidor utilizando o protocolo tcp para a  
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

# Cria um socket TCP
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Faz o bind do socket com o endereço e porta especificados
tcpSocket.bind((HOST, PORT))

# Coloca o socket em modo de escuta
tcpSocket.listen()

print('Servidor rodando...')

# Loop infinito para aceitar conexões
while True:
    # Aguarda a conexão de um cliente
    conn, address = tcpSocket.accept()
    print(f'Conexão estabelecida com {address}')

    # Loop para receber mensagens do cliente
    while True:
        # Recebe a mensagem do cliente
        data = conn.recv(1024)

        if not data:
            # Se não receber mais dados do cliente, fecha a conexão e sai do loop interno
            conn.close()
            print(f'Conexão encerrada com {address}')
            break

        #Verificando se a requisição bate com as palavras do servidor
        response = words.get(data.decode())
        if(response == None):
            response = "not found"

        # Envia a resposta para o cliente
        conn.sendall(response.encode())
