# Cliente
import socket, os

# Criar o socket cliente:
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#  Definir o servidor e porta:
servidor = socket.gethostname()
porta = 8881
#  Arquivo que vai ser usado
nome_arquivo = input("Entre com a solicitacao do arquivo a ser baixado:")

try:
    #  Tentar a conexão via connect():
    cliente.connect( (servidor, porta) )
    #  Envio a requisição de arquivo ao servidor:
    cliente.send(nome_arquivo.encode('utf-8'))
    # 5. Receber o tamanho do arquivo solicitado:
    msg = cliente.recv(2048)
    tamanho = int(msg.decode('utf-8'))
    if tamanho >= 0:
        print(f"Arquivo {nome_arquivo} solicitado possui {tamanho} bytes.")
        #  Receber o arquivo:
        #  Abrir o arquivo de destino:
        nome_arquivo_download = f"download-{nome_arquivo}"
        arquivo = open(nome_arquivo_download, 'wb')
        # 6.2 Receber os bytes do servidor:
        bytes = cliente.recv(4096)

        while bytes:
            #  Escrever o arquivo:
            arquivo.write(bytes)
            os.system('cls')
            #  Receber mais bytes:
            bytes = cliente.recv(4096)
        # Fechar o arquivo
        print(f"Download do arquivo {nome_arquivo_download} ({tamanho/1024:>.2f} KB) realizado com sucesso.")
        arquivo.close()
    else:
        print(f"Arquivo {nome_arquivo} não encontrado no servidor {servidor}...")
except Exception as erro:
    print(str(erro))