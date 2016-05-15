import gc
import asyncio
import threading

from .node import Node
from .networking import KademliaUDPServer, KademliaUDPClient


class Kademlia(object):
    def __init__(self, host, port, register_to=None, k=20):
        self.data = {}

        self.node = Node(host, port, k)
        self.received_jobs = []

        self.receiver = KademliaUDPServer(self)
        self.receiver.start()

        self.sender = KademliaUDPClient(self)

        if register_to:
            self.register(register_to)

    def register(self, gateway):
        pass

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
            self.sender('store', to=node)(key, value)

    def ping(self, node, loop=None):
        self.sender.ping(node, loop)

    def pong(self, node, loop=None):
        self.sender.pong(node, loop)
