from .networking import KademliaUDPServer, KademliaUDPClient
from .node import Node


class Kademlia(object):
    def __init__(self, host, port, k):
        self.node = Node(host, port, k)
        self.server = KademliaUPDServer(port)
        self.data = {}

    def __getitem__(self, key):
        key = Node.hash_it(key)
        if key in self.data:
            return data[key]
        return self.find_value(key)

    def __setitem__(self, key, value):
        key = Node.hash_it(key)

        neighbors = self.find_nodes(key)
        if not neighbors:
            self.data[key] = value

        for node in neighbors:
            node.store(key, value, socket=self.server.socket, node=self.node)
