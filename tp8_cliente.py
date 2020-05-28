import socket, pickle
from tabulate import tabulate
# AF_INET = IPv4
# SOCK_STREAM = TCP
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    # Tentar se conectar ao servidor
    servidor.connect((socket.gethostname(), 9991))
    print( "1 Informação Disco "
           "2 Informcao do Processamento "
           "3 Fim de Programa ")
    # enviar a mensagem vazia só para dispertar o servidor
    msg = input("Entre com a opçao desejada")

    # sempre preciso decodificar a mensagem
    servidor.send(msg.encode('utf-8'))
    bytes = servidor.recv(4096)
    # Recebe um conjunto de bytes, preciso tratar a lista uso pickle
    # Converter bytes em uma lista
    lista = pickle.loads(bytes)
    print(lista)

    # Biblioteca padrao Exception
except Exception as erro:
    print(str(erro))

servidor.close()
