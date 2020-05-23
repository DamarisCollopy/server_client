import socket,psutil,pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP
host = socket.gethostname()
porta = 9991
# Usado para TCP
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Usado para UDP muda
# servidor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
servidor.bind((host, porta))
# Escutar concexao usado para TCP
servidor.listen()
print((f"Servidor {host} experando conexao na porta {porta}"))
# Arquivo a ser enviado
disco = psutil.disk_usage('/')
disco_lista = {'Disco Total': (disco.total / 1024 ** 3, "GB"), 'Disco Usado': (disco.used / 1024 ** 3,"GB"), 'Disco Livre': (disco.free / 1024 ** 3,"GB")}

while True :
    # Receber a conexao do cliente TCP
    (cliente, endereco) = servidor.accept()
    print(f"Conectando a {str(endereco)}")
    # Converter uma lista para bytes
    informacao_bytes = pickle.dumps(disco_lista)
    # Enviar informação para o cliente
    cliente.send(informacao_bytes)

    # Terminar a conxao, agora quem recebe a mensagem e o servidor do cliente
    msg = cliente.recv(4)
    if msg.decode('utf-8') == 'fim':
        print(msg)
        break
    # Enviar a mensagem de encerramento
    cliente.send(msg)

cliente.close()
servidor.close()
