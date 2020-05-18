import socket,psutil,pickle

# AF_INET = IPv4
# SOCK_STREAM = TCP
host = socket.gethostname()
porta = 9999
servidor = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind((host, porta))
# Escutar concexao
servidor.listen()
print((f"Servidor {host} experando conexao na porta {porta}"))

(cliente, endreco) = servidor.accept()
print(f"Conectando a {str(endreco)}")

while True :
    # Receber a conexao do cliente
    mens = cliente.recv(4)
    # Terminar a conxao
    if mens.decode('utf-8') == 'Fim de Programa !':
        break
    resposta = []
    disco = psutil.disk_usage('/')
    disco_livre = disco.free / 1024 ** 3, 2
    disco_total = disco.total / 1024 ** 3, 2
    resposta.append(disco_livre)
    resposta.append(disco_total)
    # Converter uma lista para bytes
    bytes = pickle.dump(resposta)
    cliente.send(bytes)

cliente.close()
servidor.close()
