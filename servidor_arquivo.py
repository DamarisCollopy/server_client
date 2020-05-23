import socket, os


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
porta = 8881

servidor.bind( (host,porta) )

servidor.listen()
print(f"servidor {host} esperando conexão na porta {porta}...")

while True:
    #  Estabelecida a conexão com o cliente:
    (cliente, endereco) = servidor.accept()
    print(f"Conectado a {endereco}...")
    #  Receber solicitação de arquivo do cliente:
    msg = cliente.recv(2048)
    nome_arquivo = msg.decode('utf-8')
    print(f"Solicitado o arquivo {nome_arquivo}...")
    if os.path.isfile(nome_arquivo):
        # Enviar o tamanho do arquivo para o cliente:
        tamanho = os.stat(nome_arquivo).st_size
        cliente.send(str(tamanho).encode('utf-8'))
        #  Quebrar o arquivo em pacotes e enviá-lo para o cliente:
        #  Abrir o arquivo
        arquivo = open(nome_arquivo, 'rb')
        # Ler x bytes do arquivo
        bytes = arquivo.read(4096)
        while bytes:
            # Enviar os 4KB lidos
            cliente.send(bytes)
            # Ler mais 4KB
            bytes = arquivo.read(4096)
        # Fechar o arquivo
        arquivo.close()
    else: # O arquivo não existe:
        print("O arquivo solicitado não existe")
        cliente.send('-1'.encode('utf-8'))
    # Fechar o socket do cliente
    cliente.close()
# Fechar o socket do servidor
servidor.close()