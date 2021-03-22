import random
import socket
from threading import Thread
import time
import configparser


class GossipNode:
    # contém nós infectados
    infected_nodes = []

    # método de inicialização.
    # passa a porta do nó e as portas dos nós conectados a ele
    def __init__(self):
        config = configparser.RawConfigParser()
        #config.read(sys.argv[1])
        infected_nodes = [3010]

        for x in infected_nodes:
            config.read('C:/config'+ str(random.choice(infected_nodes)) +'.properties')
            port = config.get('config', 'port')
            print(port)

            # portas dos vizinhos conectados a este node
            neighbors = config.get('config', 'neighbors')
            neighbors = neighbors.split("[")
            neighbors = neighbors[1].split("]")
            neighbors = neighbors[0].split(",")

            connected_nodes = neighbors


            # criar uma nova instância de soquete
            # use SOCK_DGRAM para poder enviar dados sem uma conexão
            # sendo estabelecido (protocolo sem conexão)
            self.node = socket.socket(type=socket.SOCK_DGRAM)

            # definir o endereço, ou seja (nome do host e porta) do soquete
            self.hostname = socket.gethostname()
            self.port = port

            # ligar o endereço ao soquete criado
            self.node.bind((self.hostname, int(self.port)))

            # definir as portas dos nós conectados a ele como nós suscetíveis
            self.susceptible_nodes = connected_nodes

            print("Nó iniciado na porta {0}".format(self.port))
            print("Nós conhecidos =>", self.susceptible_nodes)

            # chame os tópicos para começar a mágica
            self.start_threads()

    def transmit_message(self):
        # loop, enquanto houver portas (nós) suscetíveis (conectadas) para enviar para
        while self.susceptible_nodes:
            # selecione uma porta aleatória da lista de nós suscetíveis
            # self.susceptible_nodes = self.susceptible_nodes.split("[")
            # self.susceptible_nodes = self.susceptible_nodes[1].split("]")
            # self.susceptible_nodes = self.susceptible_nodes[0].split(",")
            selected_port = random.choice(self.susceptible_nodes)

            print("\n")
            print("-"*50)
            print("Nós conhecidos =>", self.susceptible_nodes)
            print("Nós infectados =>", GossipNode.infected_nodes)
            print("A porta selecionada é [{0}]".format(selected_port))

            # remove o nó para o qual a mensagem foi enviada,
            # da lista de nós suscetíveis e
            # adicione-o à lista de nós infectados
            self.susceptible_nodes.remove(selected_port)
            GossipNode.infected_nodes.append(selected_port)

            print("Menssagem enviada para porta:", selected_port)
            print("Nós conhecidos =>", self.susceptible_nodes)
            print("Nós infectados =>", GossipNode.infected_nodes)
            print("-"*50)
            time.sleep(2)
            print("\n")

    def start_threads(self):
        # dois tópicos para inserir e receber uma mensagem.
        # irá permitir que cada nó seja capaz de
        # insira uma mensagem e ainda será capaz de receber uma mensagem
        Thread(target=self.transmit_message).start()
        #Thread(target=self.receive_message).start()