from .base import BaseClient


class KademliaUDPClient(BaseClient):
    def start(self):
        print("Staring sever")

    def send(self):
        return lambda x,y: print(x,y)
