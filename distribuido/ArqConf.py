# pip install configparser
import configparser
import sys
import Gossip

def Main():
    config = configparser.RawConfigParser()
    #config.read(sys.argv[1])
    #config.read('C:/config'+'2'+'.properties')

    #port = config.get('config', 'port')
    #print(port)

    # portas dos vizinhos conectados a este node
    #neighbors = config.get('config', 'neighbors')
    #neighbors = neighbors.split("[")
    #neighbors = neighbors[1].split("]")
    #neighbors = neighbors[0].split(",")

    Gossip.GossipNode()

if __name__ == '__main__':
    Main()
