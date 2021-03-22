import socket
import threading
import codecs

def handle_client(client_socket):
    while True:
        # recebe a mensagem pelo socket do cliente e ja decodifica ela
        data = client_socket.recv(1024).decode()
        if not data: 
            print("Fechando Conexão")
            break
        print('Cliente enviou: ')
        # separa os conteudos entre \r\n para ficar mais pratico de trabalhar
        mensagem = data.split('\r\n')
        # Mostra de forma bonitinha
        for msg in mensagem:
            print(msg)
        pegar_metodo = data.split('/ HTTP/1.1') # separa o metodo da mensagem
        
        if "POST" in pegar_metodo[0]: # verifica se o metodo é de POST
            mensagem.reverse() # Inverte a lista
            mensagem = mensagem[0]  # pega o item de indice 0
            mensagem = mensagem.split('&') # separa o item pelo &          
            getNome = mensagem[0].split('=') # pega o conteudo usuario=admin e separa pelo '='
            getSenha = mensagem[1].split('=') # pega o conteudo senha=admin e separa pelo '='
            nome = getNome[1] # pega o usuario
            senha = getSenha[1] # pega a senha
            try:
                if (nome == 'admin') and (senha == 'admin'): # verifica se o nome de usuario e senha estao corretos
                    # retorna uma resposta em HTML com o codigo HTTP 200 OK
                    resposta = "HTTP/1.0 200 OK\r\nContent-type:text/html;charset=utf8\r\n\r\n<html><body>Usuário logado com sucesso!</body></html>"
                    respostaFinal = resposta.encode('utf-8')
                    client_socket.send(respostaFinal)   
                    print('200 OK!')  
                else:
                    # retorna uma resposta em HTML com o codigo HTTP 400 de não autorizado
                    resposta = "HTTP/1.0 401 Unauthorized\r\nContent-type:text/html;charset=utf8\r\n\r\n<html><body>Usuario ou senha incorretos!</body></html>"
                    respostaFinal = resposta.encode('utf-8')
                    client_socket.send(respostaFinal)  
                    print('404 Unauthorized')
            except:
                print('Erro')
    client_socket.close()

def Main(): 
    host = ''
    port = 80

    # Aqui, criamos o nosso mecanismo de Socket para receber a conexão, onde na função passamos 2 argumentos,
    # AF_INET que declara a família do protocolo; se fosse um envio via Bluetooth por exemplo, seria: AF_BLUETOOTH.
    # SOCKET_STREAM, indica que será TCP/IP.
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Estas duas linhas define para qual IP e porta o servidor deve aguardar a conexão.
    s.bind((host, port))
    # Define o limite de conexões.
    s.listen(1)
  
    print("Servidor inicializado na porta " + str(port))

    while True:
        client_socket, addr = s.accept()
        print('Conexão de: ' + str(addr))
        #_thread.start_new_thread(handle_client ,(client_socket,))
        thrd = threading.Thread(target=handle_client, args=[client_socket])
        thrd.start()

if __name__ == '__main__': 
    Main()