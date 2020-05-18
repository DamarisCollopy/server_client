import socket, pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP

servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try :
    # Tentar se conectar ao servidor
    servidor.connect((socket.gethostname(), 9999))
    msg = ' '
    print(f"{'%Disco Total' :> 10}{'%Disco Usado' :>10}{'%Disco Livre' :> 10 }")
    # enviar a mensagem vazia só para dispertar o servidor
    # sempre preciso decodificar a mensagem
    servidor.send(msg.encode('utf-8'))
    bytes = servidor.recv(1024)
    # Recebe um conjunto de bytes, preciso tratar a lista uso pickle
    # Converter bytes em uma lista
    lista = pickle.load(bytes)
    texto = ' '
    for elemento in lista :
        texto += f"{elemento:> 10.2f}"
        print(texto)
    msg = 'Fim de Programa !'
    servidor.send(msg.encode('utf-8'))
    # Biblioteca padrao Exception 
except Exception as erro:
    print(str(erro))