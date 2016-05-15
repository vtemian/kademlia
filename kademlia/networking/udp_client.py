import json
import socket

from kademlia.node import Node

from .base import BaseClient


class KademliaUDPClient(BaseClient):
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self, node, data, loop=None):
        if isinstance(node, Node):
            address = node.address
        else:
            address = node.node.address

        self.socket.sendto(json.dumps(data).encode(), address)
