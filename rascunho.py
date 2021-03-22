def receive_message(self):
        while True:
            # já que estamos usando protocolo sem conexão,
            # nós usaremos 'recvfrom' para receber mensagem UDP
            message_to_forward, address = self.node.recvfrom(1024)

            # remova a porta (nó) de onde veio a mensagem,
            # da lista de nós suscetíveis e
            # adicione-o à lista de nós infectados
            self.susceptible_nodes.remove(address[0])
            GossipNode.infected_nodes.append(address[0])

            # dorme por 2 segundos para mostrar a diferença no tempo
            time.sleep(2)

            # imprimir mensagem com a hora atual.
            # decodificar a mensagem para imprimi-la, como foi enviada
            print("\nA menssagem é: '{0}'.\nRecebida de [{1}] para [{2}]\n"
                  .format(message_to_forward.decode('ascii'), time.ctime(time.time()), address[1]))

            # chamar enviar mensagem para encaminhar a mensagem para outros nós suscetíveis (conectados)
            self.transmit_message(message_to_forward)