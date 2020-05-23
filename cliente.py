import socket, pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    # Tentar se conectar ao servidor
    servidor.connect((socket.gethostname(), 9991))

    # enviar a mensagem vazia só para dispertar o servidor
    msg = ' '
    # sempre preciso decodificar a mensagem
    servidor.send(msg.encode('utf-8'))
    bytes = servidor.recv(1024)

    # Recebe um conjunto de bytes, preciso tratar a lista uso pickle
    # Converter bytes em uma lista
    lista = pickle.loads(bytes)
    print(lista)
    # Mensagem para encerramento do programa
    msg = 'fim'
    servidor.send(msg.encode('utf-8'))

    # Biblioteca padrao Exception
except Exception as erro:
    print(str(erro))

servidor.close()
input("Escreva fim para encerrar programa...")

