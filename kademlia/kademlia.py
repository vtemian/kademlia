import gc
import asyncio

import uvloop

from .node import Node
from .networking import KademliaUDPServer, KademliaUDPClient


class Kademlia(object):
    def __init__(self, host, port, register_to=None, k=20):
        self.data = {}
        self.node = Node(host, port, k)

        self.receiver = KademliaUDPServer(self)
        self.received_jobs = []
        self.sender = KademliaUDPClient(self)

        self._start(register_to)

    def _start(self, register_to=None):
        loop = uvloop.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            self.receiver.start(loop)
            self.sender.start(loop)

            if regiter:
                self.register(register_to)
            loop.run_forever()
        finally:
            loop.close()

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

    def ping(self, node):
        self.sender.ping(node)
