import socket,psutil,pickle,time

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

def processador() :
    global dic_processos
    try:
        dic_processos = {}
        for procurar in psutil.process_iter(['name', 'status']):
            if procurar.info['status'] == psutil.STATUS_RUNNING:
                if procurar.name() not in dic_processos:
                    dic_processos[procurar.name()] = {'Nome do Processo': procurar.info['name'], 'Status': procurar.info['status']}
    except:
        pass

    return dic_processos

def uso_disco():
    disco = psutil.disk_usage('/')
    disco_lista = {'Hora Inicio ':time.ctime(),'Disco Total': (disco.total / 1024 ** 3, "GB"), 'Disco Usado': (disco.used / 1024 ** 3, "GB"),
                   'Disco Livre': (disco.free / 1024 ** 3, "GB")}
    return disco_lista

while True :
    # Receber a conexao do cliente TCP
    (cliente, endereco) = servidor.accept()
    print(f"Conectando a {str(endereco)}")

    # Terminar a conxao, agora quem recebe a mensagem e o servidor do cliente
    msg = cliente.recv(4)
    if msg.decode('utf-8') == '1':
        uso = uso_disco()
        informacao_disco = pickle.dumps(uso)
        cliente.send(informacao_disco)
    elif msg.decode('utf-8') == '2':
        processos = processador()
        informacao_processos = pickle.dumps(processos)
        cliente.send(informacao_processos)
    elif msg.decode('utf-8') == '3':
        msg = "Programa encerrado"
        fim = pickle.dumps(msg)
        cliente.send(fim)
        break

cliente.close()
servidor.close()