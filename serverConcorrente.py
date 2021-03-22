import socket
import os
import sys
HOST = '127.0.0.1'   # Endereco IP do Servidor
PORT = 80            # Porta que o Servidor esta

#cria um serversocket e o define como protocolo tcp
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#define o host e a porta que o servidor vai escutar
tcp.bind((HOST, PORT))
# inica o server socket, ouvindo no maximo 5 requisiçoes de conexão
tcp.listen(5)


while True:
    con, cliente = tcp.accept()
    pid = os.fork()
    if pid == 0:
        tcp.close()
        print('Conectado por', cliente)
        while True:
            msg = con.recv(1024)
            if not msg: break
            print(cliente, msg)
        print('Finalizando conexao do cliente', cliente)
        con.close()
        sys.exit(0)
    else:
        con.close()
